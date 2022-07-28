from .base import *

print("Using development settings")

DEBUG = True

INTERNAL_IPS = ('127.0.0.1', )

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}