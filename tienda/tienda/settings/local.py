from .base import *

import firebase_admin
from firebase_admin import credentials


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'USER': get_secret('USER'),
        'PORT': get_secret('PORT'),
        'NAME': get_secret('DB_NAME'),
        'PASSWORD': get_secret('PASSWORD'),
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

# configuracion de firebase
credentials = credentials.Certificate('fbkey.json')
firebase_admin.initialize_app(credentials)