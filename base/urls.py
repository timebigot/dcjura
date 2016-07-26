from django.conf.urls import url, include, patterns
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^join', views.join, name='join'),
    url(r'^login', views.log_in, name='login'),
    url(r'^signup', views.sign_up, name='signup'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^c/(?P<url_code>\w{7})/$', views.coupon, name='coupon'),
    url(r'^map/$', views.map, name='map'),
]
