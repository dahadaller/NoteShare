<<<<<<< HEAD
# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-08 22:05
from __future__ import unicode_literals
=======
# Generated by Django 2.0.5 on 2018-12-08 23:58
>>>>>>> bd719373d8dbfc40b09b3b52f4eea85c136d2856

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creationDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ordUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
