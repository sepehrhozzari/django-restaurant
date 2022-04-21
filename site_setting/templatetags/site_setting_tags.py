from django import template
from ..models import SiteSetting
from django.shortcuts import get_object_or_404
from django.utils.html import format_html, strip_tags


register = template.Library()


@register.simple_tag
def site_title(striptags=False):
    global site_setting
    try:
        site_setting = SiteSetting.objects.get(pk=1)
    except:
        site_setting = SiteSetting.objects.create(
            pk=1,
            site_title="شاه <span>برگر</span>",
            homepage_thumbnail_text1="بهترین <span>کیفیت</span>",
            homepage_thumbnail_text2="بهترین <span>شف ها</span>",
            homepage_thumbnail_text3="بهترین <span>طعم ها</span>",
            homepage_thumbnail_description1="لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ",
            homepage_thumbnail_description2="لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ",
            homepage_thumbnail_description3="لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ",
            work_address="تهران، انقلاب، خیابان لورم، کوچه لورم",
            phone_number="09385297354",
            email_address="sepehrhozzari99@gmail.com",
            footer_text="لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ، و با استفاده از طراحان گرافیک است، چاپگرها و متون بلکه روزنامه و مجله در ستون و سطرآنچنان که لازم است، و برای شرایط فعلی تکنولوژی مورد نیاز، و کاربردهای متنوع با هدف بهبود ابزارهای کاربردی می باشد، کتابهای زیادی در شصت و سه درصد گذشته حال و آینده، شناخت فراوان جامعه و متخصصان را می طلبد، تا با نرم افزارها شناخت بیشتری را برای طراحان رایانه ای علی الخصوص طراحان خلاقی، و فرهنگ پیشرو در زبان فارسی ایجاد کرد، در این صورت می توان امید داشت که تمام و دشواری موجود در ارائه راهکارها، و شرایط سخت تایپ به پایان رسد و زمان مورد نیاز شامل حروفچینی دستاوردهای اصلی، و جوابگوی سوالات پیوسته اهل دنیای موجود طراحی اساسا مورد استفاده قرار گیرد.",
            twitter_address="https://twitter.com/Sepehrhozzari2",
            youtube_address="https://www.youtube.com/channel/UCrvVekhjmz9Kca-BHyn-Wzw",
            instagram_address="https://www.instagram.com/sepehrhozzari/",
            linkedin_address="https://www.linkedin.com/in/sepehr-hozzari-51294b226/",
        )
    if striptags:
        return strip_tags(site_setting.site_title)
    else:
        return format_html(site_setting.site_title)


@register.inclusion_tag("site_setting/partials/footer_addresses.html")
def footer_addresses():
    return {"site_setting": site_setting}


@register.inclusion_tag("site_setting/partials/carousel_items.html")
def carousel_items():
    return {"site_setting": site_setting}


@register.simple_tag
def footer_text():
    return format_html(site_setting.footer_text)
