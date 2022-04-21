from django.contrib import admin
from .models import Cart, CartItem
from restaurant.templatetags.restaurant_tags import persian_price_word


class CartAdmin(admin.ModelAdmin):
    list_display = ("title", "is_paid", "jpaid_time", "persian_discount_price")
    list_filter = (["is_paid", "paid_time", "user"])

    def persian_discount_price(self, obj):
        return persian_price_word(obj.total_discount_price)
    persian_discount_price.short_description = "کل قیمت با تخفیف"


class CartItemAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "is_paid",
                    "persian_price", "persian_discount_price")
    list_filter = (["is_paid"])

    def persian_price(self, obj):
        return persian_price_word(obj.total_price)
    persian_price.short_description = "کل قیمت"

    def persian_discount_price(self, obj):
        return persian_price_word(obj.total_discount_price)
    persian_discount_price.short_description = "کل قیمت با تخفیف"


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
