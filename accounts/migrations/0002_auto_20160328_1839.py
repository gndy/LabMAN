# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 18:39
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statuslabels',
            options={'verbose_name': 'status label', 'verbose_name_plural': 'status labels'},
        ),
        migrations.AlterField(
            model_name='department',
            name='description',
            field=tinymce.models.HTMLField(default='&nbsp;'),
        ),
        migrations.AlterField(
            model_name='jobtitle',
            name='description',
            field=tinymce.models.HTMLField(default='&nbsp;'),
        ),
        migrations.AlterField(
            model_name='statuslabels',
            name='description',
            field=tinymce.models.HTMLField(default='&nbsp;'),
        ),
        migrations.AlterField(
            model_name='title',
            name='description',
            field=tinymce.models.HTMLField(default='&nbsp;'),
        ),
    ]
