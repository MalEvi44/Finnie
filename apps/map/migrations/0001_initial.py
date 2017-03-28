# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 03:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Наименование')),
            ],
            options={
                'verbose_name_plural': 'Округа',
                'verbose_name': 'Округ',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='regions', to='map.District')),
            ],
            options={
                'verbose_name_plural': 'Районы',
                'verbose_name': 'Район',
                'ordering': ('name',),
            },
        ),
    ]
