# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlsandbookmarks', '0007_auto_20160405_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='archived',
            field=models.NullBooleanField(default=False),
        ),
    ]
