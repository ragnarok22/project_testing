from .base import *

SECRET_KEY = os.getenv("SECRET_KEY")

ALLOWED_HOSTS = ["*"]
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("DB_NAME", "django"),
        'HOST': os.getenv("DB_HOST", "db"),
        'PORT': os.getenv("DB_PORT", 5432),
        'USER': os.getenv("DB_USER", "django"),
        'PASSWORD': os.getenv("DB_PASSWORD", "django"),

    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
