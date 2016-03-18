# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailtemplate',
            name='ref',
            field=models.PositiveSmallIntegerField(unique=True, verbose_name='Gabarit', choices=[(1, 'Account creation'), (2, 'Password reset'), (3, 'Order'), (4, 'Contact'), (5, 'Partner contact')]),
        ),
    ]
