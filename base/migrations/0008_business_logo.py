# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_coupon_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='logo',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
