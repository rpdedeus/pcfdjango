import os
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG')

ALLOWED_HOSTS = ['pcfdjango.cfapps.io']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

ENGINE = os.environ.get('DB_ENGINE')
NAME = os.environ.get('DB_NAME')
USER = os.environ.get('DB_USER')
PASSWORD = os.environ.get('DB_PASSWORD')
HOST = os.environ.get('DB_HOST')
PORT = os.environ.get('DB_PORT')

DATABASES = {
    'default': {
        'USER': USER,
        'PASSWORD': PASSWORD,
        'NAME': NAME,
        'HOST': HOST,
        'PORT': PORT,
        'ENGINE': ENGINE,
    }
}
