from django.urls import path
from .views import (
    home,
    BookTable,
    Contact,
    About,
    Chefs,
    Search,
    Category,
    FoodDetail,
    food_api,
    like,
    dislike,
)


app_name = "restaurant"
urlpatterns = [
    path('', home, name="home"),
    path('book-table', BookTable.as_view(), name="book_table"),
    path('contact/', Contact.as_view(), name="contact"),
    path('about/', About.as_view(), name="about"),
    path('chefs/', Chefs.as_view(), name="chefs"),
    path('search/', Search.as_view(), name="search"),
    path('search/page/<int:page>', Search.as_view(), name="search"),
    path('category/<int:pk>/<title>', Category.as_view(), name="category"),
    path('category/<int:pk>/<title>/page/<int:page>',
         Category.as_view(), name="category"),
    path('food/<int:pk>/<name>',
         FoodDetail.as_view(), name="food_detail"),
    path('api/<int:pk>', food_api, name="food_api"),
    path('api/<int:pk>/like', like, name="like"),
    path('api/<int:pk>/dislike', dislike, name="dislike"),
]
