# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 01:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urlsandbookmarks', '0002_auto_20160401_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='clicks',
        ),
    ]