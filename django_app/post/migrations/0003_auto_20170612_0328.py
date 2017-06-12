# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 03:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20170612_0327'),
    ]

    operations = [
        migrations.AddField(
            model_name='postlike',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='postlike',
            table=None,
        ),
    ]
