# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-27 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChaRate', '0012_auto_20180327_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='comments',
            field=models.IntegerField(default=0),
        ),
    ]
