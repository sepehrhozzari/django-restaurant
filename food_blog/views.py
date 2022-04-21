from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Article
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


class ArticleList(ListView):
    paginate_by = 4
    queryset = Article.objects.optimazed().published()


class ArticleDetail(DetailView):
    def get_object(self):
        pk = self.kwargs.get("pk")
        food = get_object_or_404(
            Article.objects.optimazed().published(), pk=pk)

        ip_address = self.request.user.ip_address
        if ip_address not in food.hits.all():
            food.hits.add(ip_address)

        return food


@login_required
def article_api(request, pk):
    user = request.user
    article = get_object_or_404(Article.objects.published(), pk=pk)
    return JsonResponse({
        "likes": article.likes.count(),
        "dislikes": article.dislikes.count(),
        "is_authenticated": user.is_authenticated,
    })


@login_required
def like(request, pk):
    user = request.user
    article = get_object_or_404(Article.objects.published(), pk=pk)
    if user in article.dislikes.all():
        article.dislikes.remove(user)
        if user in article.likes.all():
            article.likes.remove(user)
        else:
            article.likes.add(user)
    else:
        if user in article.likes.all():
            article.likes.remove(user)
        else:
            article.likes.add(user)
    return redirect("restaurant:home")


@login_required
def dislike(request, pk):
    user = request.user
    article = get_object_or_404(Article.objects.published(), pk=pk)
    if user in article.likes.all():
        article.likes.remove(user)
        if user in article.dislikes.all():
            article.dislikes.remove(user)
        else:
            article.dislikes.add(user)
    else:
        if user in article.dislikes.all():
            article.dislikes.remove(user)
        else:
            article.dislikes.add(user)
    return redirect("restaurant:home")
