# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 09:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('title', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='title',
            name='actor',
            field=models.ManyToManyField(to='title.Actor'),
        ),
        migrations.AddField(
            model_name='title',
            name='director',
            field=models.ManyToManyField(to='title.Director'),
        ),
        migrations.AddField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(to='title.Genre'),
        ),
        migrations.AddField(
            model_name='title',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='title.Type'),
        ),
        migrations.AddField(
            model_name='rating',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='title.Title'),
        ),
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='favourite',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='title.Title'),
        ),
        migrations.AddField(
            model_name='favourite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='watchlist',
            unique_together=set([('user', 'title')]),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set([('user', 'title', 'rate_date')]),
        ),
        migrations.AlterUniqueTogether(
            name='favourite',
            unique_together=set([('user', 'title')]),
        ),
    ]
