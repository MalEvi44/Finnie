# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 14:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.IntegerField(choices=[(1, 'Основной'), (2, 'Показатель')], verbose_name='Тип документа')),
                ('description', models.TextField(unique=True, verbose_name='Наименование')),
                ('description_imp', models.TextField(unique=True, verbose_name='Наименование (повелительное)')),
            ],
            options={
                'verbose_name': 'Документ-основание',
                'verbose_name_plural': 'Документы-основания',
            },
        ),
        migrations.CreateModel(
            name='MonthlyRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_negotiated', models.BooleanField(default=False, verbose_name='Согласован')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Утвержден')),
                ('year', models.SmallIntegerField(choices=[(2016, 2016), (2017, 2017), (2018, 2018)], verbose_name='Год')),
                ('month', models.SmallIntegerField(choices=[(1, 'Январь'), (2, 'Февраль'), (3, 'Март'), (4, 'Апрель'), (5, 'Май'), (6, 'Июнь'), (7, 'Июль'), (8, 'Август'), (9, 'Сентябрь'), (10, 'Октябрь'), (11, 'Ноябрь'), (12, 'Декабрь')], verbose_name='Месяц')),
                ('approved_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.PrefectureEmployee', verbose_name='Утвердивший сотрудник')),
                ('base_document', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ratings.BaseDocument', verbose_name='Документ-основание')),
            ],
            options={
                'verbose_name': 'Месячный рейтинг',
                'verbose_name_plural': 'Месячные рейтинги',
                'ordering': ('-year', '-month'),
            },
        ),
        migrations.CreateModel(
            name='MonthlyRatingElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_description', models.TextField(blank=True, null=True, verbose_name='Дополнительное описание')),
                ('negotiator_comment', models.TextField(blank=True, null=True, verbose_name='Комментарий согласовывающего')),
                ('region_comment', models.TextField(blank=True, null=True, verbose_name='Комментарий района')),
                ('monthly_rating', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='elements', to='ratings.MonthlyRating', verbose_name='Месячный рейтинг')),
            ],
            options={
                'verbose_name': 'Компонент месячного рейтинга',
                'verbose_name_plural': 'Компоненты месячного рейтинга',
            },
        ),
        migrations.CreateModel(
            name='MonthlyRatingSubElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('date', models.DateField(blank=True, null=True)),
                ('description', models.TextField()),
                ('best_type', models.SmallIntegerField(choices=[(1, 'мин'), (2, 'макс')])),
                ('document', models.FileField(upload_to='uploads/%Y/%m/%d/documents/')),
                ('monthly_rating_element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_sub_elements', to='ratings.MonthlyRatingElement')),
                ('responsible', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.PrefectureEmployee')),
            ],
            options={
                'verbose_name': 'Подкомпонент месячного рейтинга',
                'verbose_name_plural': 'Подкомпоненты месячных рейтингов',
            },
        ),
        migrations.CreateModel(
            name='MonthlyRatingSubElementValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_average', models.BooleanField(default=False)),
                ('value', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('monthly_rating_sub_element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='ratings.MonthlyRatingSubElement')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.Region')),
            ],
            options={
                'verbose_name': 'Значение подкомпонента месячного рейтинга',
                'verbose_name_plural': 'Значения подкомпонентов месячных рейтингов',
            },
        ),
        migrations.CreateModel(
            name='RatingElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(verbose_name='№ п/п')),
                ('name', models.TextField(verbose_name='Наименование')),
                ('base_description', models.TextField(blank=True, null=True, verbose_name='Базовое описание')),
                ('weight', models.SmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], verbose_name='Вес')),
                ('sub_elements_display_type', models.SmallIntegerField(choices=[(1, 'десятичное число'), (2, 'процент')], verbose_name='Тип отображения подкомпонентов')),
                ('valid_from_month', models.SmallIntegerField(choices=[(1, 'Январь'), (2, 'Февраль'), (3, 'Март'), (4, 'Апрель'), (5, 'Май'), (6, 'Июнь'), (7, 'Июль'), (8, 'Август'), (9, 'Сентябрь'), (10, 'Октябрь'), (11, 'Ноябрь'), (12, 'Декабрь')], db_index=True, verbose_name='Действует с месяца')),
                ('valid_from_year', models.SmallIntegerField(choices=[(2016, 2016), (2017, 2017), (2018, 2018)], db_index=True, verbose_name='Действует с года')),
                ('valid_to_month', models.SmallIntegerField(blank=True, choices=[(1, 'Январь'), (2, 'Февраль'), (3, 'Март'), (4, 'Апрель'), (5, 'Май'), (6, 'Июнь'), (7, 'Июль'), (8, 'Август'), (9, 'Сентябрь'), (10, 'Октябрь'), (11, 'Ноябрь'), (12, 'Декабрь')], db_index=True, null=True, verbose_name='Действует по месяц(включительно)')),
                ('valid_to_year', models.SmallIntegerField(blank=True, choices=[(2016, 2016), (2017, 2017), (2018, 2018)], db_index=True, null=True, verbose_name='Действует по год(включительно)')),
                ('base_document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratings.BaseDocument', verbose_name='Документ-основание')),
                ('responsible', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.PrefectureEmployee', verbose_name='Ответственный (базовый)')),
            ],
            options={
                'verbose_name': 'Базовый компонент рейтинга',
                'verbose_name_plural': 'Базовые компоненты рейтинга',
                'ordering': ('number',),
            },
        ),
        migrations.CreateModel(
            name='SignerText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(unique=True, verbose_name='Текст')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активный')),
            ],
            options={
                'verbose_name': 'Текст подписанта',
                'verbose_name_plural': 'Тексты подписантов',
            },
        ),
        migrations.AddField(
            model_name='monthlyratingelement',
            name='rating_element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ratings.RatingElement', verbose_name='Базовый компонент рейтинга'),
        ),
        migrations.AddField(
            model_name='monthlyratingelement',
            name='responsible',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.PrefectureEmployee', verbose_name='Ответственный'),
        ),
        migrations.AddField(
            model_name='monthlyrating',
            name='signer_text',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ratings.SignerText', verbose_name='Текст подписанта'),
        ),
        migrations.AlterUniqueTogether(
            name='monthlyratingsubelementvalue',
            unique_together=set([('region', 'monthly_rating_sub_element')]),
        ),
        migrations.AlterUniqueTogether(
            name='monthlyratingsubelement',
            unique_together=set([('name', 'date')]),
        ),
        migrations.AlterUniqueTogether(
            name='monthlyratingelement',
            unique_together=set([('monthly_rating', 'rating_element')]),
        ),
        migrations.AlterUniqueTogether(
            name='monthlyrating',
            unique_together=set([('year', 'month')]),
        ),
    ]
