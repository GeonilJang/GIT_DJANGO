# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-07-05 07:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FoodAdmin',
            new_name='Food',
        ),
    ]
