# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-26 22:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ChaRate', '0003_character_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='written_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('sci', 'Sci-Fi'), ('action', 'Action'), ('horror', 'Horror'), ('comedy', 'Comedy'), ('romance', 'Romance'), ('other', 'Other')], max_length=20),
        ),
        migrations.AlterField(
            model_name='tv',
            name='genre',
            field=models.CharField(choices=[('sci', 'Sci-Fi'), ('action', 'Action'), ('horror', 'Horror'), ('comedy', 'Comedy'), ('romance', 'Romance'), ('other', 'Other')], max_length=20),
        ),
    ]
