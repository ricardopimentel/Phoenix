# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-30 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_virtualizacao_id_equipamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='virtualizacao',
            name='arquitetura',
            field=models.CharField(choices=[('32', '32 bits'), ('64', '64 bits')], default=64, max_length=60, verbose_name='Arquitetura'),
            preserve_default=False,
        ),
    ]
