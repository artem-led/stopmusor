# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-21 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_papers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default=b'New', verbose_name=b'Service title')),
                ('foto', models.TextField(default=b'Foto', verbose_name=b'Way to foto')),
                ('foto_title', models.TextField(default=b'Foto', verbose_name=b'Foto title')),
                ('author', models.TextField(default=b'Author', verbose_name=b'Service Author')),
                ('body', models.TextField(default=b'Body', verbose_name=b'Service body')),
                ('posted', models.DateField(auto_now_add=True, db_index=True)),
            ],
            options={
                'ordering': ['posted'],
            },
        ),
    ]