from django.db import models
from account.models import User
from restaurant.models import Food
from django.db.models import Prefetch
from extensions.utils import jalali_converter


class CartItemQuerySet(models.query.QuerySet):
    def optimazed(self):
        return self.select_related("user", "item")


class CartItemManager(models.Manager):
    def get_queryset(self):
        return CartItemQuerySet(self.model, using=self._db)

    def optimazed(self):
        return self.get_queryset().optimazed()


class CartItem(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cartitems", verbose_name="کاربر")
    item = models.ForeignKey(
        Food, on_delete=models.CASCADE, verbose_name="محصول")
    quantity = models.PositiveSmallIntegerField(
        default=1, verbose_name="تعداد")
    is_paid = models.BooleanField(default=False, verbose_name="پرداخت شده")

    def __str__(self):
        return f"{self.quantity} عدد از {self.item}"

    objects = CartItemManager()

    class Meta:
        ordering = ["-is_paid"]
        verbose_name = "آیتم سبد خرید"
        verbose_name_plural = "آیتم های سبد خرید"

    @property
    def total_discount_price(self):
        return self.item.discount_price * self.quantity

    @property
    def total_price(self):
        return self.item.price * self.quantity

    def title(self):
        return f"{self.quantity} عدد از {self.item}"
    title.short_description = "محصول"


class CartQuerySet(models.query.QuerySet):
    def optimazed(self):
        return self.prefetch_related(Prefetch(
            "items", queryset=CartItem.objects.select_related("user", "item")
        )).select_related("user")


class CartManager(models.Manager):
    def get_queryset(self):
        return CartQuerySet(self.model, using=self._db)

    def optimazed(self):
        return self.get_queryset().optimazed()


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="کاربر", related_name="carts")
    items = models.ManyToManyField(CartItem, verbose_name="محصولات")
    is_paid = models.BooleanField(default=False, verbose_name="پرداخت شده")
    paid_time = models.DateTimeField(verbose_name="زمان پرداخت")

    objects = CartManager()

    class Meta:
        ordering = ["-is_paid"]
        verbose_name = "سبد خرید"
        verbose_name_plural = "سبد خرید کاربران"

    def __str__(self):
        return f"سبد خرید کاربر {self.user.username}"

    @property
    def total_discount_price(self):
        total = 0
        for cart_item in self.items.all():
            total += cart_item.total_discount_price
        return total

    @property
    def total_price(self):
        total = 0
        for cart_item in self.items.all():
            total += cart_item.total_price
        return total

    def title(self):
        return f"سبد خرید کاربر {self.user.username}"
    title.short_description = "کاربر"

    def jpaid_time(self):
        if not self.paid_time:
            return "-"
        return jalali_converter(self.paid_time)
    jpaid_time.short_description = "تاریخ پرداخت"
