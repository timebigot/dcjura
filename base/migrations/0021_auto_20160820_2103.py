# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-21 01:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_query_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='query_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
