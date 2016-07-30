from django import template
from django.conf import settings as base_set
import datetime

register = template.Library()

@register.simple_tag
def gmaps():
    keys = base_set.GMAPS_KEY
    return keys

@register.filter
def expire_soon(exp_day):
    today = datetime.date.today()
    two_day = datetime.timedelta(days=2)
    if exp_day - today < two_day:
        return True
    else:
        return False

