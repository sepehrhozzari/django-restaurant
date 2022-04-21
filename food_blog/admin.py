from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "thumbnail_tag", "status", "jpublish",
                    "author", "hit_count", "like_count", "comment_count")
    list_filter = ("status", "publish", "author")
    search_fields = ("title", "description")

    def hit_count(self, obj):
        return obj.hits.count()
    hit_count.short_description = "تعداد بازدید ها"

    def like_count(self, obj):
        return obj.likes.count()
    like_count.short_description = "تعداد لایک ها"

    def comment_count(self, obj):
        return obj.comments.count()
    comment_count.short_description = "تعداد کامنت ها"


admin.site.register(Article, ArticleAdmin)
