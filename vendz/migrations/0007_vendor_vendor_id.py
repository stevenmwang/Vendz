# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-18 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendz', '0006_vendor_occurances'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='vendor_id',
            field=models.IntegerField(default=0),
        ),
    ]
