from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from datetime import datetime

class Category(models.Model):
    eng_name = models.CharField(max_length=20)
    kor_name = models.CharField(max_length=20)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.eng_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.eng_name

class Business(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    owner = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    logo = models.FileField(upload_to='logo/', blank=True)
    is_active = models.BooleanField(default=1)

    def __str__(self):
        return self.name

class Coupon(models.Model):
    title = models.TextField(max_length=100)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    exp_date = models.DateField(blank=True, null=True)
    url_code = models.CharField(max_length=7)
    cover = models.FileField(upload_to='cover/')
    link = models.CharField(max_length=200, blank=True)
    is_void = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Query(models.Model):
    query = models.CharField(max_length=50)
    query_time = models.DateTimeField(default=datetime.now, blank=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.query

class View(models.Model):
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    view_time = models.DateTimeField(default=datetime.now, blank=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return '%s - %s' % (self.coupon, self.view_time)
