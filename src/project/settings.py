import os
from pathlib import Path

import dj_database_url
from dynaconf import settings

from framework.dirs import DIR_TEMPLATES

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = settings.SECRET_KEY

DEBUG = settings.MODE_DEBUG

ALLOWED_HOSTS = [
    "max-tms10.herokuapp.com",
    "localhost",
    "127.0.0.1",
]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'applications.index.apps.IndexConfig',
    'applications.blog.apps.BlogConfig',
    'applications.task306.apps.Task306Config',
    'applications.task307.apps.Task307Config',
    'applications.task308.apps.Task308Config',
    'applications.task310.apps.Task310Config',
    'applications.task311.apps.Task311Config',
    'applications.task402.apps.Task402Config',
    'applications.task404.apps.Task404Config',
    'applications.task406.apps.Task406Config',
    'applications.task407.apps.Task407Config',
    'applications.task501.apps.Task501Config',
    'applications.task502.apps.Task502Config',
    'applications.task503.apps.Task503Config',
    'applications.task504.apps.Task504Config',
    'applications.task507.apps.Task507Config',
    'applications.task702.apps.Task702Config',
    'applications.task703.apps.Task703Config',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [DIR_TEMPLATES],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


database_url = os.getenv("DATABASE_URL", settings.DATABASE_URL)
DATABASES = {
    'default': dj_database_url.parse(database_url),
    }


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
] if not DEBUG else []


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
