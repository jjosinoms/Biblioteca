# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-03-13 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0003_auto_20180313_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='biblioteca/uploads/'),
        ),
    ]
