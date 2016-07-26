from django.db import models
from django.conf import settings

class Business(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, blank=True)
    owner = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100)
    logo = models.FileField(upload_to='logo/')
    is_active = models.BooleanField(default=1)

    def __str__(self):
        return self.name

class Coupon(models.Model):
    title = models.CharField(max_length=50)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    exp_date = models.CharField(max_length=20, blank=True)
    url_code = models.CharField(max_length=7)
    cover = models.FileField(upload_to='cover/')
    is_void = models.BooleanField(default=False)

    def __str__(self):
        return self.title
