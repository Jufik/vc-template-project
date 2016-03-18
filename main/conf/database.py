DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': '{{ cookiecutter.db_name }}',
        'USER': '{{ cookiecutter.db_user }}',
        'PASSWORD': '{{ cookiecutter.db_password }}',
        'HOST': 'HOST',
        'PORT': '5432',
    }
}


