# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-01 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups_manager', '0004_0_6_0_groupmember_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmember',
            name='expiration_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
