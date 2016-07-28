from django import template
from django.conf import settings as base_set

register = template.Library()

@register.simple_tag
def gmaps():
    keys = base_set.GMAPS_KEY
    return keys
