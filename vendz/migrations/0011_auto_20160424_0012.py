# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendz', '0010_remove_event_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='occurances',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='vendor_id',
        ),
        migrations.AlterField(
            model_name='vendor',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
