# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-02 08:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0007_auto_20180602_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapobjects',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 2, 8, 5, 17, 274310)),
        ),
    ]