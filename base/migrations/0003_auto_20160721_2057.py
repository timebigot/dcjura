# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20160721_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='business',
            name='owner',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
