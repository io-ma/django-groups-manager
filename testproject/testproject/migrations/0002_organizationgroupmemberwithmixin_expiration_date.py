# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-19 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testproject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationgroupmemberwithmixin',
            name='expiration_date',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]