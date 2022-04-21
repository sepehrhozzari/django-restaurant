from django.db import models
from django.utils.html import format_html
from django.db.models import Prefetch
from account.models import User, IPAddress
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from django.urls import reverse
from extensions.utils import jalali_converter


class CategoryQuerySet(models.query.QuerySet):
    def optimazed(self):
        return self.select_related("parent")

    def active(self):
        return self.filter(status=True)


class CategoryManager(models.Manager):
    def get_queryset(self):
        return CategoryQuerySet(self.model, using=self._db)

    def optimazed(self):
        return self.get_queryset().optimazed()

    def active(self):
        return self.get_queryset().active()


class Category(models.Model):
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,
                               related_name="children", verbose_name="زیر‌دسته")
    title = models.CharField(max_length=100, verbose_name="عنوان")
    image = models.ImageField(upload_to="images")
    status = models.BooleanField(
        default=True, verbose_name="آیا نمایش داده شود")
    position = models.IntegerField(verbose_name="پوزیشن")

    def __str__(self):
        return self.title

    objects = CategoryManager()

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    @property
    def slug(self):
        return self.title.replace(" ", "-")

    def image_tag(self):
        return format_html(f"<img class='rounded' style='width: 150px;' src='{self.image.url}'>")
    image_tag.short_description = "تصویر"


class FoodQuerySet(models.query.QuerySet):
    def optimazed(self):
        return self.prefetch_related(Prefetch("category", queryset=Category.objects.optimazed().active())).select_related("chef")

    def active(self):
        return self.filter(status=True)


class FoodManager(models.Manager):
    def get_queryset(self):
        return FoodQuerySet(self.model, using=self._db)

    def optimazed(self):
        return self.get_queryset().optimazed()

    def active(self):
        return self.get_queryset().active()


class Food(models.Model):
    chef = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="foods", verbose_name="آشپز")
    category = models.ManyToManyField(
        Category, related_name="foods", verbose_name="دسته‌بندی")
    name = models.CharField(max_length=150, verbose_name="اسم")
    image = models.ImageField(upload_to="images", verbose_name="عکس")
    description = models.TextField(verbose_name="توضیحات")
    status = models.BooleanField(default=True, verbose_name="موجود")
    price = models.FloatField(verbose_name="قیمت")
    discount_price = models.FloatField(default=0, verbose_name="قیمت با تخفیف")
    likes = models.ManyToManyField(
        User, related_name="likes", blank=True, verbose_name="لایک")
    dislikes = models.ManyToManyField(
        User, related_name="dislikes", blank=True, verbose_name="دیس لایک")
    hits = models.ManyToManyField(
        IPAddress, through="FoodHit", related_name="hits", verbose_name="بازدید ها")
    comments = GenericRelation(Comment)

    def __str__(self):
        return self.name

    objects = FoodManager()

    class Meta:
        verbose_name = "غذا"
        verbose_name_plural = "غذاها"

    def check_super_sell(self):
        if self.price - self.discount_price >= 50000:
            return True
        return False

    @property
    def slug(self):
        return self.name.replace(" ", "-")

    def image_tag(self):
        return format_html(f"<img class='rounded' style='width: 100px;' src='{self.image.url}'>")
    image_tag.short_description = "تصویر"


class FoodHit(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IPAddress, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class BookTable(models.Model):
    GUEST_CHOICES = (
        ('1', 'یک نفر'),
        ('2', 'دو نفر'),
        ('3', 'سه نفر'),
        ('4', 'چهار نفر'),
        ('5', 'پنج نفر'),
        ('6', 'شیش نفر'),
        ('7', 'هفت نفر'),
        ('8', 'هشت نفر'),
        ('9', 'نه نفر'),
        ('10', 'ده نفر'),
        ('11', 'یازده نفر'),
        ('12', 'دوازده نفر'),
        ('13', 'سیزده نفر'),
        ('14', 'چهارده نفر'),
        ('15', 'پانزده نفر'),
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booked_tables", verbose_name="کاربر")
    date = models.DateTimeField(verbose_name="تاریخ")
    phone_number = models.DecimalField(
        max_digits=11, decimal_places=0, verbose_name="شماره تلفن")
    guest = models.CharField(
        max_length=2, choices=GUEST_CHOICES, verbose_name="تعداد مهمان ها")

    def __str__(self):
        return f"سفارش رزرو میز برای کاربر {self.user}"

    class Meta:
        verbose_name = "سفارش رزرو میز"
        verbose_name_plural = "سفارش ها برای رزرو میز"

    def get_absolute_url(self):
        return reverse("account:booked_tables")

    def jdate(self):
        return jalali_converter(self.date)
    jdate.short_description = "تاریخ"


class ContactMessage(models.Model):
    user = models.ForeignKey(
        User, null=True, on_delete=models.SET_NULL, related_name="sended_contact_messages", verbose_name="کاربر")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="زمان فرستادن")
    subject = models.CharField(verbose_name="موضوع", max_length=200)
    message = models.TextField(verbose_name="پیام")

    def __str__(self):
        return f"پیام کاربر {self.user}"

    class Meta:
        verbose_name = "پیام ارسال شده برای پشتیبانی"
        verbose_name_plural = "پیام های ارسال شده برای پشتیبانی"

    def jcreated(self):
        return jalali_converter(self.created)
    jcreated.short_description = "تاریخ فرستادن پیام"

    def get_absolute_url(self):
        return reverse("account:sended_contact_messages")
