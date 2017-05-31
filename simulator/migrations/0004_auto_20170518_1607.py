# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 14:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simulator', '0003_buildingfloors_local_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carsNumber', models.IntegerField(default=0)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulator.Building')),
            ],
        ),
        migrations.AlterField(
            model_name='buildingfloors',
            name='entry',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='buildingfloors',
            name='interfloor',
            field=models.FloatField(default=3),
        ),
    ]