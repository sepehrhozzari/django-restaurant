from django.urls import path
from .views import add_to_cart, cart_item_delete, single_cart_item_delete, CartSummary, payment


app_name = "cart"
urlpatterns = [
    path("add-to-cart/<int:pk>/<name>", add_to_cart, name="add_to_cart"),
    path("remove-from-cart/<int:pk>/<name>",
         cart_item_delete, name="remove_from_cart"),
    path("single-cart-item-delete/<int:pk>/<name>", single_cart_item_delete,
         name="single_cart_item_delete"),
    path("cart-summary/", CartSummary.as_view(), name="cart_summary"),
    path("payment/", payment, name="payment"),
]
