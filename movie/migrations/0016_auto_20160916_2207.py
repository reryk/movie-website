# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-16 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0015_auto_20160916_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='const',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
