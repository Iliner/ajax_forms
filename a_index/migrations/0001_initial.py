# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 13:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30, unique=True)),
                ('articul', models.CharField(max_length=30)),
                ('producer', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('in_stock', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.FloatField()),
                ('order_count', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('photo_width', models.IntegerField(default=0)),
                ('photo_height', models.IntegerField(default=0)),
                ('photo', models.ImageField(upload_to='')),
                ('code', models.IntegerField()),
                ('image_url', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
                'ordering': ['date'],
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='a_index.Photo'),
        ),
        migrations.AlterUniqueTogether(
            name='goods',
            unique_together=set([('code', 'articul')]),
        ),
    ]
