# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-04 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_rank',
            field=models.IntegerField(default=-1),
        ),
    ]