import datetime

# Check:
# http://condopilot.com/blog/web/how-setup-gzip-compressor-and-aws-s3-django/

S3_ENDPOINT = 'https://{{ cookiecutter.project_name }}.s3.amazonaws.com/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = '{{ cookiecutter.aws_access_key_id }}'
AWS_SECRET_ACCESS_KEY = '{{ cookiecutter.aws_secret_key_id }}'
AWS_STORAGE_BUCKET_NAME = '{{ cookiecutter.project_name }}'
AWS_S3_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME
AWS_S3_CALLING_FORMAT = 'boto.s3.connection.OrdinaryCallingFormat'
# We are not using SSL. You can change this to "True" and to "https:"
# if you are using a SSL Certificate.
AWS_S3_SECURE_URLS = False
AWS_S3_URL_PROTOCOL = 'http:'

AWS_IS_GZIPPED = True
GZIP_CONTENT_TYPES = (
 'text/css',
 'application/javascript',
 'application/x-javascript',
 'text/javascript'
)
# http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
expiry_time = datetime.datetime.utcnow() + datetime.timedelta(days=360)  # 1year
expires_header = expiry_time.strftime("%a, %d %b %Y %H:%M:%S GMT")
AWS_HEADERS = {
    'Expires': expires_header,
    'Cache-Control': 'max-age=31556926',  # 1year
}

COMPRESS_ENABLED = True
COMPRESS_CSS_FILTERS = ['compressor.filters.css_default.CssAbsoluteFilter', 'compressor.filters.cssmin.CSSMinFilter']