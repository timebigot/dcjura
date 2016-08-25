from . import views
from django.conf.urls import url, include, patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^coupon/(?P<url_code>\w{7})/$', views.coupon, name='coupon'),
    url(r'^category/(?P<category>\w+)/$', views.category, name='category'),
    url(r'^process/(?P<url_code>\w{7})/$', views.process, name='process'),
    url(r'^search$', views.search, name='search_redirect'),
    url(r'^search/(?P<query>[^\/]+)/$', views.search, name='search'),
    url(r'^numbers$', views.numbers, name='numbers'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^scraper$', views.scraper, name='scraper'),
    url(r'^adminpost$', views.adminpost, name='adminpost'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
