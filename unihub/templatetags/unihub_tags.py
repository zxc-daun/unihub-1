from django import template
from unihub.models import *

register = template.Library()


@register.simple_tag()
def get_categories():
    return ClubCategory.objects.all()


@register.inclusion_tag('unihub/list_categories.html')
def show_categories():
    categories = ClubCategory.objects.all()
    return {"categories": categories}

