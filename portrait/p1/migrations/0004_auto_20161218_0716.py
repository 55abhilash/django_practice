# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-18 07:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p1', '0003_auto_20161217_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='pwd',
            field=models.CharField(max_length=128),
        ),
    ]
