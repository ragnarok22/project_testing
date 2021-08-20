from .base import *

SECRET_KEY = os.getenv("SECRET_KEY")

ALLOWED_HOSTS = ["*"]
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("DB_NAME"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),

    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
