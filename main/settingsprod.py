import os
import raven

from main.settings import *

DEBUG = False
ALLOWED_HOSTS = ['*']

INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATIC_URL = S3_ENDPOINT

RAVEN_CONFIG = {
    # 'release': raven.fetch_git_sha(os.path.dirname(__file__)),
}