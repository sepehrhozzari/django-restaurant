from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from restaurant.models import Food
from .models import CartItem, Cart
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.utils import timezone


@login_required
def add_to_cart(request, pk, name):
    item = get_object_or_404(Food.objects.active(), pk=pk)
    try:
        cart_item = CartItem.objects.get(
            user=request.user, item=item, is_paid=False)
    except:
        cart_item = CartItem.objects.create(user=request.user, item=item)
    try:
        cart = Cart.objects.get(user=request.user, is_paid=False)
    except:
        cart = Cart.objects.create(user=request.user, is_paid=False)
    if cart.items.filter(item__pk=item.pk).exists():
        cart_item.quantity += 1
        cart_item.save()
        messages.info(
            request, f"تعداد {item} افزایش یافت")
        return redirect("cart:cart_summary")
    else:
        cart.items.add(cart_item)
        messages.info(
            request, f"{item} به سبد خرید شما اضافه شد")
        return redirect("cart:cart_summary")


@login_required
def cart_item_delete(request, pk, name):
    item = get_object_or_404(Food.objects.active(), pk=pk)
    try:
        cart = Cart.objects.get(user=request.user, is_paid=False)
    except:
        cart = Cart.objects.create(user=request.user, is_paid=False)
    if cart.items.filter(item__pk=item.pk).exists():
        cart_item = CartItem.objects.get(
            user=request.user,
            item=item,
            is_paid=False
        )
        cart_item.delete()
        messages.warning(request, f"{item} از سبد خرید حذف شد")
        return redirect("cart:cart_summary")
    else:
        return redirect("cart:cart_summary")


@login_required
def single_cart_item_delete(request, pk, name):
    item = get_object_or_404(Food.objects.active(), pk=pk)
    try:
        cart = Cart.objects.get(user=request.user, is_paid=False)
    except:
        cart = Cart.objects.create(user=request.user, is_paid=False)
    if cart.items.filter(item__pk=item.pk).exists():
        cart_item = CartItem.objects.get(
            user=request.user,
            item=item,
            is_paid=False
        )
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
            messages.warning(
                request, f"تعداد {item} کمتر شد")
            return redirect("cart:cart_summary")
        else:
            return redirect(reverse(
                "cart:remove_from_cart", kwargs={"pk": pk, "name": name}))
    else:
        return redirect("cart:cart_summary")


class CartSummary(LoginRequiredMixin, DetailView):
    template_name = "cart/cart_summary.html"

    def get_object(self):
        try:
            return Cart.objects.optimazed().get(user=self.request.user, is_paid=False)
        except:
            return Cart.objects.optimazed().create(user=self.request.user, is_paid=False)


@login_required
def payment(request):
    try:
        cart = request.user.carts.get(is_paid=False)
    except:
        cart = Cart.object.create(user=request.user, is_paid=False)
    if cart.items.all().exists():
        cart.is_paid = True
        cart.paid_time = timezone.now()
        for cart_item in cart.items.all():
            cart_item.is_paid = True
            cart_item.save()
        cart.save()
        messages.success(request, "پرداخت با موفقیت انجام شد")
        return redirect("cart:cart_summary")
    else:
        messages.info(request, "شما محصولی در سبد خرید ندارید")
        return redirect("cart:cart_summary")
