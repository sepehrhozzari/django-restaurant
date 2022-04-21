from django.contrib import admin
from .models import SiteSetting


class SiteSettingAdmin(admin.ModelAdmin):
    fieldsets = (
        ("هدر سایت", {"fields": ("homepage_thumbnail_text1", "homepage_thumbnail_text2", "homepage_thumbnail_text3",
         "homepage_thumbnail_description1", "homepage_thumbnail_description2", "homepage_thumbnail_description3", "site_title")}),
        ("فوتر سایت", {"fields": ("work_address",
         "phone_number", "email_address", "footer_text")}),
        ("لینک اکانت های سوشال مدیا", {"fields": (
            "twitter_address", "youtube_address", "instagram_address", "linkedin_address")})
    )


admin.site.register(SiteSetting, SiteSettingAdmin)
