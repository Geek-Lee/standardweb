# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_aritcle'),
    ]

    operations = [
        migrations.AddField(
            model_name='aritcle',
            name='tag',
            field=models.CharField(blank=True, choices=[('tech', 'Tech'), ('life', 'Life')], max_length=5, null=True),
        ),
    ]
