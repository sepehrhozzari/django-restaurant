from django.shortcuts import render, get_object_or_404, redirect
from .mixins import BookTableMixin
from django.views.generic import (
    CreateView,
    TemplateView,
    ListView,
    DetailView,
)
from .forms import BookTableForm
from .models import ContactMessage
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
)
from .models import Food, Category as Ctg
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def home(request):
    return render(request, 'restaurant/home.html')


class BookTable(BookTableMixin, CreateView):
    form_class = BookTableForm
    template_name = "restaurant/book_table.html"


class Contact(CreateView):
    template_name = "restaurant/contact.html"
    model = ContactMessage
    fields = ["subject", "message"]

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.user = self.request.user
        return super().form_valid(form)


class About(TemplateView):
    template_name = "restaurant/about.html"


class Chefs(TemplateView):
    template_name = "restaurant/chefs.html"


class Search(ListView):
    template_name = "restaurant/search.html"
    paginate_by = 1

    def get_queryset(self):
        global search
        search = self.request.GET.get("search_queryset")
        vector = SearchVector("name", "description")
        query = SearchQuery(search)
        food_qs = Food.objects.active().annotate(
            rank=SearchRank(vector, query)).filter(rank__gt=0.001).order_by('-rank')
        return food_qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search"] = search
        return context


class Category(ListView):
    template_name = "restaurant/category.html"
    paginate_by = 2

    def get_queryset(self):
        global category
        pk = self.kwargs.get('pk')
        category = get_object_or_404(
            Ctg.objects.active(), pk=pk)
        return category.foods.active().annotate(count=Count("likes")).order_by("-count")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


class FoodDetail(DetailView):
    def get_object(self):
        pk = self.kwargs.get('pk')
        food = Food.objects.optimazed().get(pk=pk)

        ip_address = self.request.user.ip_address
        if ip_address not in food.hits.all():
            food.hits.add(ip_address)

        return food


@login_required
def food_api(request, pk):
    user = request.user
    food = get_object_or_404(Food.objects.active(), pk=pk)
    return JsonResponse({
        "likes": food.likes.count(),
        "dislikes": food.dislikes.count(),
        "is_authenticated": user.is_authenticated,
    })


@login_required
def like(request, pk):
    user = request.user
    food = get_object_or_404(Food.objects.active(), pk=pk)
    if user in food.dislikes.all():
        food.dislikes.remove(user)
        if user in food.likes.all():
            food.likes.remove(user)
        else:
            food.likes.add(user)
    else:
        if user in food.likes.all():
            food.likes.remove(user)
        else:
            food.likes.add(user)
    return redirect("restaurant:home")


@login_required
def dislike(request, pk):
    user = request.user
    food = get_object_or_404(Food.objects.active(), pk=pk)
    if user in food.likes.all():
        food.likes.remove(user)
        if user in food.dislikes.all():
            food.dislikes.remove(user)
        else:
            food.dislikes.add(user)
    else:
        if user in food.dislikes.all():
            food.dislikes.remove(user)
        else:
            food.dislikes.add(user)
    return redirect("restaurant:home")
