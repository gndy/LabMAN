# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 17:09
from __future__ import unicode_literals

import colorful.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', tinymce.models.HTMLField()),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='equipment', to='locations.Location')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Owned_Equipment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'equipment',
            },
        ),
        migrations.CreateModel(
            name='Equipment_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', tinymce.models.HTMLField()),
                ('status', colorful.fields.RGBColorField()),
            ],
            options={
                'verbose_name': 'equipment status label',
            },
        ),
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.Equipment')),
            ],
        ),
        migrations.CreateModel(
            name='UserList_level',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('description', tinymce.models.HTMLField()),
                ('level', models.IntegerField(primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name': 'user level label',
            },
        ),
        migrations.AddField(
            model_name='userlist',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='equipment.UserList_level'),
        ),
        migrations.AddField(
            model_name='userlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userOf', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='equipment',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.Equipment_Status'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='users',
            field=models.ManyToManyField(through='equipment.UserList', to=settings.AUTH_USER_MODEL),
        ),
    ]
