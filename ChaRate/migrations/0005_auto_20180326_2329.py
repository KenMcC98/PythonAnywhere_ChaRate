# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-26 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChaRate', '0004_auto_20180326_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='writer',
            field=models.CharField(max_length=150),
        ),
    ]