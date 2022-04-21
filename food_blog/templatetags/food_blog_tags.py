from django import template
from datetime import datetime, timedelta
from ..models import Article
from django.db.models import Count, Q


register = template.Library()


@register.inclusion_tag("food_blog/partials/latest_articles.html")
def latest_articles():
    return {"articles": Article.objects.optimazed().published()[:2]}


@register.inclusion_tag("food_blog/partials/sidebar_widget.html")
def sidebar_widget():
    last_week = datetime.today() - timedelta(days=7)
    return {"popular_articles": Article.objects.published().annotate(
        count=Count("hits", filter=Q(articlehit__created__gt=last_week))
    ).order_by("-count")}
