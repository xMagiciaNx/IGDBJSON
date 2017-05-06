# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 00:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GamesDB', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='GameIsMultiplayer',
            field=models.BooleanField(default=1, verbose_name='Multiplayer?'),
            preserve_default=False,
        ),
    ]
