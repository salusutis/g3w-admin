# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-10 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qdjango', '0035_auto_20180910_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widget',
            name='widget_type',
            field=models.CharField(choices=[(b'search', 'Search')], max_length=255, verbose_name='Type'),
        ),
    ]
