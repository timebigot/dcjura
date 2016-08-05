from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

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
    phone = models.CharField(max_length=15)
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
    is_void = models.BooleanField(default=False)

    def __str__(self):
        return self.title
