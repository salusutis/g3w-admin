# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-15 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iternet', '0026_auto_20160415_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='comuni',
            name='cod_istat',
            field=models.CharField(max_length=6, null=True),
        ),
    ]