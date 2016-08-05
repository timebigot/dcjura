from django.contrib import admin
from .models import *

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('eng_name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Business)
admin.site.register(Coupon)
