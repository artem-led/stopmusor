# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-19 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='New', verbose_name='Question title')),
                ('fio', models.TextField(default='', verbose_name='Question User Name')),
                ('email', models.TextField(default='', verbose_name='Question User email')),
                ('body', models.TextField(default='', verbose_name='Question Body')),
                ('posted', models.DateField(auto_now_add=True, db_index=True)),
            ],
            options={
                'ordering': ['posted'],
            },
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['posted']},
        ),
    ]