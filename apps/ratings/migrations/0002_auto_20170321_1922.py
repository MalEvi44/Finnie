# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratingelement',
            name='sub_elements_display_type',
        ),
        migrations.AddField(
            model_name='monthlyratingsubelement',
            name='display_type',
            field=models.SmallIntegerField(choices=[(1, 'десятичное число'), (2, 'процент')], default=1),
        ),
        migrations.AlterField(
            model_name='monthlyratingsubelementvalue',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=8, null=True),
        ),
    ]
