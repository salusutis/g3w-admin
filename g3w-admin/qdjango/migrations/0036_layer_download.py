# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-06 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qdjango', '0035_auto_20180910_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='layer',
            name='download',
            field=models.BooleanField(default=False, verbose_name='Download data'),
        ),
    ]
