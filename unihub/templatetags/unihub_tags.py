from django import template
from unihub.models import *

register = template.Library()


@register.simple_tag()
def get_categories():
    return ClubCategory.objects.all()
