# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-03-15 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0005_auto_20180315_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='sinopse',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]