# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GamesDB', '0007_publisher_publisherlogo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='GameRating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='1', max_length=3, verbose_name='Rating'),
        ),
    ]
