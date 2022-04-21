from django.db import models


class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class SiteSetting(SingletonModel):

    # header settings
    site_title = models.CharField(verbose_name="متن اصلی سایت", max_length=200)
    homepage_thumbnail_text1 = models.CharField(
        verbose_name="متن عکس صفحه‌ی اصلی سایت شماره ۱", max_length=200)
    homepage_thumbnail_text2 = models.CharField(
        verbose_name="متن عکس صفحه‌ی اصلی سایت شماره ۲", max_length=200)
    homepage_thumbnail_text3 = models.CharField(
        verbose_name="متن عکس صفحه‌ی اصلی سایت شماره ۳", max_length=200)

    homepage_thumbnail_description1 = models.TextField(
        verbose_name="توضیحات عکس صفحه‌ی اصلی سایت شماره ۱")
    homepage_thumbnail_description2 = models.TextField(
        verbose_name="توضیحات عکس صفحه‌ی اصلی سایت شماره ۲")
    homepage_thumbnail_description3 = models.TextField(
        verbose_name="توضیحات عکس صفحه‌ی اصلی سایت شماره ۳")

    # footer settings
    work_address = models.CharField(
        max_length=300, verbose_name="آدرس محل کار")
    phone_number = models.CharField(max_length=11, verbose_name="شماره تلفن")
    email_address = models.EmailField(
        blank=True, verbose_name="آدرس ایمیل")
    footer_text = models.TextField(verbose_name="متن فوتر")

    # social account address setting
    twitter_address = models.URLField(
        max_length=200, verbose_name="آدرس اکانت تویتر")
    youtube_address = models.URLField(
        max_length=200, verbose_name="آدرس اکانت یوتیوب")
    instagram_address = models.URLField(
        max_length=200, verbose_name="آدرس اکانت اینستاگرام")
    linkedin_address = models.URLField(
        max_length=200, verbose_name="آدرس اکانت لینکدین")

    class Meta:
        verbose_name = "تنظیمات سایت"
        verbose_name_plural = "تنظیمات سایت"
