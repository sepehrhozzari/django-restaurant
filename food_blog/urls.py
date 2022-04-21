from django.urls import path
from .views import ArticleList, ArticleDetail, article_api, like, dislike


app_name = "food_blog"
urlpatterns = [
    path("articles/", ArticleList.as_view(), name="article_list"),
    path("articles/page/<int:page>", ArticleList.as_view(), name="article_list"),
    path("article/<int:pk>/<title>",
         ArticleDetail.as_view(), name="article_detail"),
    path('api/<int:pk>', article_api, name="article_api"),
    path('api/<int:pk>/like', like, name="like"),
    path('api/<int:pk>/dislike', dislike, name="dislike"),
]
