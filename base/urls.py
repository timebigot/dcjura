from . import views
from django.conf.urls import url, include, patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^coupon/(?P<url_code>\w{7})/$', views.coupon, name='coupon'),
    url(r'^category/(?P<category>\w+)/$', views.category, name='category'),
    url(r'^modal/(?P<url_code>\w{7})/$', views.modal, name='modal'),
    url(r'^search$', views.search, name='search_redirect'),
    url(r'^search/(?P<query>[^\/]+)/$', views.search, name='search'),
    url(r'^numbers$', views.numbers, name='numbers'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
