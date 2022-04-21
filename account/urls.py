from django.urls import path
from .views import (
    Signup,
    activate,
    Dashboard,
    Profile,
    Address,
    CartHistory,
    BookedTables,
    SendedContactMessages,
    DeleteAccount,
)

app_name = "account"
urlpatterns = [
    path('signup/', Signup.as_view(), name="signup"),
    path('activate/<uidb64>/<token>', activate, name="activate"),
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('profile/', Profile.as_view(), name="profile"),
    path('address/', Address.as_view(), name="address"),
    path('cart-history', CartHistory.as_view(), name="cart_history"),
    path('cart-history/page/<int:page>',
         CartHistory.as_view(), name="cart_history"),
    path('booked-tables/', BookedTables.as_view(), name="booked_tables"),
    path('sended_contact_messages/', SendedContactMessages.as_view(),
         name="sended_contact_messages"),
    path('delete-account/', DeleteAccount.as_view(), name="delete_account"),
]
