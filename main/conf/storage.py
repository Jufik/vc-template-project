import datetime

S3_ENDPOINT = 'https://{{ cookiecutter.project_name }}.s3.amazonaws.com/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = '{{ cookiecutter.aws_access_key_id }}'
AWS_SECRET_ACCESS_KEY = '{{ cookiecutter.aws_secret_key_id }}'
AWS_STORAGE_BUCKET_NAME = '{{ cookiecutter.project_name }}'


# http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
expiry_time = datetime.datetime.utcnow() + datetime.timedelta(days=360)  # 1year
expires_header = expiry_time.strftime("%a, %d %b %Y %H:%M:%S GMT")
AWS_HEADERS = {
    'Expires': expires_header,
    'Cache-Control': 'max-age=31556926',  # 1year
}
