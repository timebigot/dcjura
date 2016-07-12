from django.db import models
from django.conf import settings

class Business(models.Model):
    business_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    owner = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    is_active = models.BooleanField(default=1)
   
class Coupon(models.Model):
    title = models.CharField(max_length=50)
    business = models.CharField(max_length=50)
    about = models.CharField(max_length=100)
    expire_date = models.CharField(max_length=20)
    is_void = models.BooleanField(default=0)
    
