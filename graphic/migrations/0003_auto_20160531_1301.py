# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-31 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graphic', '0002_auto_20160520_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivo',
            name='arq',
            field=models.FileField(upload_to='/home/suelliton/projetos/grafico/graphic/media'),
        ),
    ]
