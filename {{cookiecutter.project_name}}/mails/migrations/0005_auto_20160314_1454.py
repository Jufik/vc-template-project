# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0004_auto_20160314_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailtemplate',
            name='ref',
            field=models.CharField(choices=[('SIGN', "Cr\xe9ation d'un compte"), ('MAIL', "Confirmation d'adresse e-mail"), (3, 'Order Credit card')], max_length=4, unique=True, verbose_name='Gabarit'),
        ),
    ]
