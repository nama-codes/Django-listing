# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 08:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20170918_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='fav',
        ),
        migrations.AddField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]
