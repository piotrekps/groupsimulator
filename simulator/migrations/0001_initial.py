# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('floors', models.IntegerField(default=9)),
                ('floor_dist', models.IntegerField(default=3)),
                ('population', models.IntegerField(default=50)),
            ],
        ),
    ]
