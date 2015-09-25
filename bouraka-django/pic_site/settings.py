"""
Django settings for pic_site project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@z)2*9$r==sjt^d3$%chi=!rq--bszd_u53su#tzbwj1awr%$s'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = False 
DEBUG = True 

TEMPLATE_DEBUG = True
#TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = (

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'members',
    'news',

    'photologue',
    'sortedm2m',

)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)

#FOR GRAPPELLI
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
from photologue import PHOTOLOGUE_APP_DIR
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    PHOTOLOGUE_APP_DIR,
)

AUTHENTICATION_BACKENDS = (
     'django.contrib.auth.backends.ModelBackend',
)

############### TRYING GMAIL #####################

EMAIL_USER = 'pic.insa.lyon@gmail.com'
EMAIL_PASSWORD = 'protoinsaclub007'
#DEFAULT_FROM_EMAIL = 'test@protoinsaclub.tk'
##################################################

ROOT_URLCONF = 'pic_site.urls'

WSGI_APPLICATION = 'pic_site.wsgi.application'

SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
STATIC_URL = '/static/'
STATIC_ROOT='/bouraka/bouraka-static/'

MEDIAFILES_DIRS = (
    os.path.join(BASE_DIR, "media"),
)
MEDIA_URL = '/media/'
MEDIA_ROOT = '/bouraka/bouraka-media/'

#FileBrowser settings
FILEBROWSER_MAX_UPLOAD_SIZE = getattr(settings, "FILEBROWSER_MAX_UPLOAD_SIZE", 104857600)

#Grappelli settings
GRAPPELLI_ADMIN_TITLE = 'Proto INSA Club'

