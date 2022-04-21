from django.db import models
from account.models import User, IPAddress
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from extensions.utils import jalali_converter
from django.utils.html import format_html
from django.urls import reverse


class ArticleQuerySet(models.query.QuerySet):
    def optimazed(self):
        return self.prefetch_related("hits", "likes", "dislikes", "comments").select_related("author")

    def published(self):
        return self.filter(status="p")


class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def optimazed(self):
        return self.get_queryset().optimazed()

    def published(self):
        return self.get_queryset().published()


class Article(models.Model):
    STATUS_CHOICES = (
        ("p", "منتشر شده"),
        ("d", "پیش‌نویس"),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="articles", verbose_name="نویسنده")
    title = models.CharField(max_length=200, verbose_name="عنوان")
    description = models.TextField(verbose_name="محتوا")
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")
    thumbnail = models.ImageField(upload_to="images", verbose_name="تصویر")
    publish = models.DateTimeField(
        default=timezone.now, verbose_name="تاریخ انتشار")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="زمان ایجاد")
    updated = models.DateTimeField(auto_now=True, verbose_name="زمان تغییر")
    hits = models.ManyToManyField(IPAddress, through="ArticleHit",
                                  related_name="article_hits", blank=True, verbose_name="بازدید ها")
    likes = models.ManyToManyField(
        User, related_name="article_likes", blank=True, verbose_name="لایک")
    dislikes = models.ManyToManyField(
        User, related_name="article_dislikes", blank=True, verbose_name="دیس لایک")
    comments = GenericRelation(Comment)

    def __str__(self):
        return self.title

    objects = ArticleManager()

    class Meta:
        ordering = ["-publish"]
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = "تاریخ انتشار"

    def thumbnail_tag(self):
        return format_html(f"<img class='rounded' style='width: 100px;' src='{self.thumbnail.url}'>")
    thumbnail_tag.short_description = "تصویر"

    def get_absolute_url(self):
        return reverse("restaurant:home")

    @property
    def slug(self):
        return self.title.replace(" ", "-")


class ArticleHit(models.Model):
    ip_address = models.ForeignKey(IPAddress, on_delete=models.CASCADE)
    Article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
