# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_video_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='image_path',
            field=models.CharField(blank=True, default='/static/ang/assets/images/nature/4.jpg', max_length=120, null=True),
        ),
    ]
