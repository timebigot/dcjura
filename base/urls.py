from django.conf.urls import url, include, patterns
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
