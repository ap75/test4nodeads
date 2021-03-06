# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-21 19:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180221_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='checked',
            field=models.NullBooleanField(verbose_name='Проверен модератором'),
        ),
        migrations.AddField(
            model_name='element',
            name='created',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='element',
            name='descr',
            field=models.TextField(blank=True, max_length=512, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='element',
            name='icon',
            field=models.ImageField(upload_to='upload', verbose_name='Иконка'),
        ),
        migrations.AlterField(
            model_name='element',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='group',
            name='descr',
            field=models.TextField(blank=True, max_length=512, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='group',
            name='icon',
            field=models.ImageField(upload_to='upload', verbose_name='Иконка'),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='group',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_parent', to='api.Group', verbose_name='Родительская группа'),
        ),
    ]
