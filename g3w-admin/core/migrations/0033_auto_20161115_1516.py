# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-15 15:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20160920_0818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='max_scale',
        ),
        migrations.RemoveField(
            model_name='group',
            name='min_scale',
        ),
    ]
