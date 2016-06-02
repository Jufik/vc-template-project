import os
import raven

from main.settings import *

DEBUG = False
ALLOWED_HOSTS = ['*']

INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)
STATICFILES_STORAGE = 'custom_storages.CachedS3BotoStorage'
COMPRESS_STORAGE = STATICFILES_STORAGE
STATIC_URL = S3_ENDPOINT

RAVEN_CONFIG = {
    # 'release': raven.fetch_git_sha(os.path.dirname(__file__)),
    {{ cookiecutter.sentry_dsn }}
}