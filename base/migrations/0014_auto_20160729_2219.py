# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_auto_20160729_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]