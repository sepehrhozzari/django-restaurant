from django import template
from ..models import Category, Food
from datetime import datetime, timedelta
from django.db.models import Count, Q
from django.contrib.humanize.templatetags.humanize import intcomma, naturaltime


register = template.Library()


@register.inclusion_tag("restaurant/partials/nav_link.html")
def nav_link(request, link_name, content, extra_classes=""):
    return {
        "request": request,
        "content": content,
        "link_name": link_name,
        "link": f"restaurant:{link_name}",
        "extra_classes": extra_classes,
    }


@register.inclusion_tag("restaurant/partials/category_menu.html")
def category_menu():
    return {"categorys": Category.objects.active()}


@register.inclusion_tag("restaurant/partials/extra_menu.html")
def popular_foods():
    last_week = datetime.now() - timedelta(days=7)
    return {
        "foods": Food.objects.active().annotate(
            count=Count("hits", filter=Q(foodhit__created__gt=last_week)
                        )).order_by("-count")[:4],
        "title": "غذا هایی که در این هفته بیشترین بازدید را داشته اند",
    }


@register.filter(name="persian_price_word")
def persian_price_word(integer):
    integer = str(integer)
    count = 0
    for letter in integer:
        count += 1
    if count > 8:
        persian_price_word = "میلیون تومان"
    else:
        persian_price_word = "هزار تومان"
    intcomma_price = intcomma(integer).replace(".0", "")
    return f"{intcomma_price} {persian_price_word}"


@register.filter(name="p_naturaltime")
def p_naturaltime(time):
    time = naturaltime(time)
    time = time.replace("ها", "")
    return time.replace("،", "و ")
