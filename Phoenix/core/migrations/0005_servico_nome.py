# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-30 10:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20181130_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='nome',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Nome'),
            preserve_default=False,
        ),
    ]
