# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_coupon_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='cover',
            field=models.FileField(default='', upload_to=''),
        ),
    ]