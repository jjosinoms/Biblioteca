# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-03-16 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0007_auto_20180315_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='sinopse',
            field=models.TextField(max_length=500),
        ),
    ]
