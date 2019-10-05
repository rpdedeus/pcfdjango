import os
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!%b&#g#xbk=4&c+933mhstxo(3hz7e6yl@3o_ebd(%$#ld+9i('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
