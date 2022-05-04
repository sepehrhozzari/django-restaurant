from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    TemplateView,
    DeleteView
)
from .forms import SignupForm, ProfileForm, AddressForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib import messages
from .models import User
from django.contrib.auth import login
from cart.models import Cart
from django.urls import reverse_lazy


class Signup(CreateView):
    template_name = "registration/signup.html"
    form_class = SignupForm

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'فعال سازی اکانت'
        message = render_to_string('registration/activate_account.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = user.email
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        messages.info(
            self.request, "لینک فعال سازی اکانت با موفقیت به ایمیل شما ارسال شد")
        return redirect("account:signup")


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(User, pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect("account:dashboard")
    else:
        messages.info(request, "لینک منقضی شده است")
        return redirect("account:signup")


class Dashboard(LoginRequiredMixin, ListView):
    template_name = "registration/dashboard.html"

    def get_queryset(self):
        user = self.request.user
        return user.likes.active()[:6]


class Profile(LoginRequiredMixin, UpdateView):
    template_name = "registration/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy("account:profile")

    def get_object(self):
        pk = self.request.user.pk
        return get_object_or_404(User, pk=pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs


class Address(LoginRequiredMixin, UpdateView):
    template_name = "registration/address.html"
    form_class = AddressForm
    success_url = reverse_lazy("account:address")

    def get_object(self):
        pk = self.request.user.pk
        return get_object_or_404(User, pk=pk)


class CartHistory(LoginRequiredMixin, ListView):
    template_name = "registration/cart_history.html"
    paginate_by = 8

    def get_queryset(self):
        return Cart.objects.optimazed().filter(user=self.request.user, is_paid=True)


class BookedTables(LoginRequiredMixin, TemplateView):
    template_name = "registration/booked_tables.html"


class SendedContactMessages(LoginRequiredMixin, TemplateView):
    template_name = "registration/sended_contact_messages.html"


class DeleteAccount(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "registration/confirm_user_delete.html"
    success_url = reverse_lazy("login")

    def get_object(self):
        return self.request.user
