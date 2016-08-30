# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0010_auto_20160726_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommendation',
            name='c',
        ),
        migrations.AddField(
            model_name='recommendation',
            name='const',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='date_insert',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='nick',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='note',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='year',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]