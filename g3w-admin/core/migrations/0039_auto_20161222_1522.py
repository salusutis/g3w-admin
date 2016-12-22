# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-22 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_auto_20161219_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='header_terms_of_use_link',
            field=models.URLField(blank=True, verbose_name='Terms of use link'),
        ),
        migrations.AlterField(
            model_name='group',
            name='header_terms_of_use_text',
            field=models.TextField(blank=True, verbose_name='Terms of use text'),
        ),
    ]
