# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_business_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='logo',
            field=models.FileField(upload_to='logo/'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='cover',
            field=models.FileField(upload_to='cover/'),
        ),
    ]