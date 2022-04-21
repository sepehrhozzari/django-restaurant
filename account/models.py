from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    CITY_CHOICES = (
        ('TEHRAN', 'تهران'),
        ('KARAJ', 'کرج'),
        ('SHIRAZ', 'شیراز'),
        ('ESFAHAN', 'اصفهان'),
        ('YAZD', 'یزد'),
        ('AHVAZ', 'اهواز'),
        ('ARDEBIL', 'اردبیل'),
        ('TABRIZ', 'تبریز'),
        ('MASHHAD', 'مشهد'),
    )

    email = models.EmailField(unique=True, verbose_name="ایمیل")
    is_chef = models.BooleanField(default=False, verbose_name="آشپز")
    profile_picture = models.ImageField(verbose_name="عکس پروفایل", blank=True)
    bio = models.CharField(max_length=400, verbose_name="بیوگرافی", blank=True)
    city = models.CharField(
        max_length=30, choices=CITY_CHOICES, verbose_name="شهر", blank=True)
    address = models.TextField(verbose_name="آدرس", blank=True)

    def get_full_name(self):
        if not self.first_name and not self.last_name:
            return "%s" % (self.username)
        else:
            return "%s %s" % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse("account:profile")


class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name="آدرس آی پی")

    def __str__(self):
        return self.ip_address
