# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 14:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_auto_20170328_0911'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='monthlyratingelement',
            options={'ordering': ('number', 'id'), 'verbose_name': 'Компонент месячного рейтинга', 'verbose_name_plural': 'Компоненты месячного рейтинга'},
        ),
    ]