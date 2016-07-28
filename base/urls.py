from . import views
from django.conf.urls import url, include, patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^c/(?P<url_code>\w{7})/$', views.coupon, name='coupon'),
    url(r'^map/$', views.map, name='map'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
