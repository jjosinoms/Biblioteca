# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-03-21 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0008_auto_20180316_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='file',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
