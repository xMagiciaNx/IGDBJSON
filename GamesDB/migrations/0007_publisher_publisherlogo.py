# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-15 19:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GamesDB', '0006_genre_genreimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='PublisherLogo',
            field=models.ImageField(null=True, upload_to='', verbose_name='Image'),
        ),
    ]
