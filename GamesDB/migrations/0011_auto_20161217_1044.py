# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GamesDB', '0010_auto_20161217_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='GameReview',
            field=models.TextField(max_length=10000, verbose_name='Review'),
        ),
    ]
