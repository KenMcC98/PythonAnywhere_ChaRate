# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-27 16:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChaRate', '0005_auto_20180326_2329'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Profile',
        ),
    ]
