# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-23 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_transport_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='logo',
            field=models.FileField(default='music/images/2-image.jpg', upload_to='music/'),
        ),
    ]
