# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 15:30
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0005_auto_20160229_0815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('attribution', models.TextField(blank=True, verbose_name='Attributions')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from=b'name', unique=True, verbose_name='Slug')),
                ('is_active', models.BooleanField(default=1, verbose_name='Is active')),
                ('layer_type', models.CharField(choices=[(b'wms', 'WMS'), (b'wmst', b'wmst'), ('WMST', 'WMST'), (b'tms', 'TMS')], max_length=255, verbose_name='Type')),
                ('datasource', models.TextField(blank=True, verbose_name='Datasource')),
                ('layers', models.TextField(blank=True, verbose_name='Layers(WMS)')),
                ('is_visible', models.BooleanField(default=1, verbose_name='Is visible')),
                ('order', models.IntegerField(default=1, verbose_name='Order')),
            ],
            options={
                'ordering': ['order'],
                'permissions': (('view_ogc_layer', 'Can view OGC layer'),),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from=b'title', unique=True, verbose_name='Slug')),
                ('is_active', models.BooleanField(default=1, verbose_name='Is active')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=b'', verbose_name='Thumbnail')),
                ('initial_extent', models.CharField(max_length=255, verbose_name='Initial extent')),
                ('max_extent', models.CharField(max_length=255, verbose_name='Max extent')),
                ('is_panoramic_map', models.BooleanField(default=0, verbose_name='Is panoramic map')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ogc_projetc_group', to='core.Group', verbose_name='Group')),
            ],
            options={
                'permissions': (('view_ogc_project', 'Can view OGC project'),),
            },
        ),
        migrations.AddField(
            model_name='layer',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ogc.Project', verbose_name='OGC Project'),
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('title', 'group')]),
        ),
        migrations.AlterUniqueTogether(
            name='layer',
            unique_together=set([('name', 'project')]),
        ),
    ]