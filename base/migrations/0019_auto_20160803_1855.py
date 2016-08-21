# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 22:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_auto_20160730_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng_name', models.CharField(max_length=20)),
                ('kor_name', models.CharField(max_length=20)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='coupon',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Category'),
        ),
    ]