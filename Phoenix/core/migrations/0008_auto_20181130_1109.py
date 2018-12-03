# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-30 11:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20181130_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='servico_virtualizacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.servico')),
            ],
        ),
        migrations.CreateModel(
            name='virtualizacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=90, verbose_name='Descrição')),
                ('monitorado', models.CharField(choices=[('s', 'Sim'), ('n', 'Não')], max_length=50, verbose_name='Necessita Monitoramento')),
                ('status', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('id_sistema_operacional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.sistema_operacional')),
            ],
        ),
        migrations.RemoveField(
            model_name='equipamento',
            name='tipo',
        ),
        migrations.AddField(
            model_name='servico_virtualizacao',
            name='id_virtualizacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.virtualizacao'),
        ),
    ]