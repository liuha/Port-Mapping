# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-19 20:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Distance', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'unknown', max_length=25)),
                ('floor', models.IntegerField(default=3)),
                ('x_coord', models.IntegerField(null=True)),
                ('y_coord', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='edge',
            name='FromNode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_node', to='maps.Node'),
        ),
        migrations.AddField(
            model_name='edge',
            name='ToNode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_node', to='maps.Node'),
        ),
    ]
