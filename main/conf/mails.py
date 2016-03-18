# -*- coding: utf-8 -*-
from __future__ import unicode_literals

EMAIL_HOST = "{{ cookiecutter.email_host }}"
EMAIL_HOST_USER = '{{ cookiecutter.email_host_user }}'
EMAIL_HOST_PASSWORD = '{{ cookiecutter.email_host_password }}'
EMAIL_PORT = 587
EMAIL_SUBJECT_PREFIX = ""
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_SENDER = '{{ cookiecutter.email_sender }}'

EMAIL_RECIEVERS = ['{{ cookiecutter.email_recievers }}']
