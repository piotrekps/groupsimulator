# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0018_auto_20170524_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='statsimulation',
            name='step',
            field=models.FloatField(default=0),
        ),
    ]
