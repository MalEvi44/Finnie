# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 20:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    def add_sao_district(self, schema_editor):
        self.get_model("map", "District").objects.create(name='САО')

    def add_sao_regions(self, schema_editor):
        model = self.get_model("map", "Region")
        sao_district = self.get_model("map", "District").objects.get(name='САО')
        manager = model.objects
        manager.bulk_create([
            model(district=sao_district, name='Аэропорт'),
            model(district=sao_district, name='Беговой'),
            model(district=sao_district, name='Бескудниковский'),
            model(district=sao_district, name='Войковский'),
            model(district=sao_district, name='Восточное Дегунино'),
            model(district=sao_district, name='Головинский'),
            model(district=sao_district, name='Дмитровский'),
            model(district=sao_district, name='Западное Дегунино'),
            model(district=sao_district, name='Коптево'),
            model(district=sao_district, name='Левобережный'),
            model(district=sao_district, name='Молжаниновский'),
            model(district=sao_district, name='Савёловский'),
            model(district=sao_district, name='Сокол'),
            model(district=sao_district, name='Тимирязевский'),
            model(district=sao_district, name='Ховрино'),
            model(district=sao_district, name='Хорошёвский')
        ])

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
                'verbose_name': 'Округ',
                'verbose_name_plural': 'Округа',
            },
        ),
        migrations.RunPython(add_sao_district),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='regions', to='map.District')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
            },
        ),
        migrations.RunPython(add_sao_regions)
    ]
