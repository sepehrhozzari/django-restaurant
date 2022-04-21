from django.contrib import admin
from .models import Category, Food, BookTable, ContactMessage
from restaurant.templatetags.restaurant_tags import persian_price_word


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "image_tag", "status", "position")
    list_filter = (["status", "position"])
    search_fields = ("title",)


class FoodAdmin(admin.ModelAdmin):
    list_display = ("name", "image_tag", "chef",
                    "status", "persian_price", "persian_discount_price", "comment_count", "like_count", "hit_count")
    list_filter = (["status", "category", "chef"])
    search_fields = ("name", "description")

    def comment_count(self, obj):
        return obj.comments.count()
    comment_count.short_description = "تعداد کامنت ها"

    def like_count(self, obj):
        return obj.likes.count()
    like_count.short_description = "تعداد لایک ها"

    def hit_count(self, obj):
        return obj.hits.count()
    hit_count.short_description = "تعداد بازدید ها"

    def persian_price(self, obj):
        return persian_price_word(obj.price)
    persian_price.short_description = "قیمت"

    def persian_discount_price(self, obj):
        return persian_price_word(obj.price)
    persian_discount_price.short_description = "قیمت با تخفیف"


class BookTableAdmin(admin.ModelAdmin):
    list_display = ("user", "guest", "jdate", "phone_number")
    list_filter = ("date", "guest")
    search_fields = ("phone_number", "date")


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("user", "subject", "jcreated", "message")
    list_filter = ("created",)
    search_fields = ("subject", "message")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(BookTable, BookTableAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
