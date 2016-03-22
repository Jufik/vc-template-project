# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('ref', models.PositiveSmallIntegerField(unique=True, verbose_name='Gabarit', choices=[(1, 'Cr\xe9ation du compte'), (2, 'R\xe9initialisation du mot de passe'), (3, 'Payment accompte'), (4, 'Contact'), (5, 'Partner contact')])),
                ('subject', models.CharField(max_length=255, verbose_name='Objet')),
                ('html', models.TextField(help_text='Use <a href="http://templates.mailchimp.com/resources/inline-css/">CSS Inliner</a>', verbose_name='Contenu HTML')),
                ('txt', models.TextField(help_text='Use <a href="http://templates.mailchimp.com/resources/html-to-text/">HTML to Text</a>', verbose_name='Contenu TXT')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
