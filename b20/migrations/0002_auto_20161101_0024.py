# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 18:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('b20', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AliveVouchers',
            new_name='AliveVoucher',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]