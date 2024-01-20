"""
Django settings for securefileshare project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m&5l7-u*gowsgnwhxq2g-o(0xytt*k*onu*q%#+#8@31cb-64*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [".vercel.app"]
CSRF_TRUSTED_ORIGINS = [os.environ.get("CSRF_TRUSTED_ORIGINS", None)]
SELF_HOST = os.environ.get("SELF_HOST", "")


# Application definition

INSTALLED_APPS = [
    # JAZZMIN THEME FOR ADMIN
    'jazzmin',

    # DJANGO APPS
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # CLOUDINARY STORAGE
    # 'cloudinary_storage',
    # 'cloudinary',

    # THIRD PARTY APPS
    'corsheaders',
    'rest_framework',
    'django_object_actions',

    # CUSTOM APPS
    'alpha',
    'client',
    'fileshare',
    'organization',
]

MIDDLEWARE = [
    # DJANGO MIDDLEWARES
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',

    # THIRD PARTY MIDDLEWARES
    'corsheaders.middleware.CorsMiddleware',
    'threadlocals.middleware.ThreadLocalMiddleware',

    # CUSTOM MIDDLEWARES
    'alpha.middlewares.VerifyAPIKeyMiddleware',
]

ROOT_URLCONF = 'securefileshare.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'securefileshare.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("POSTGRES_DATABASE"),
        'USER': os.environ.get("POSTGRES_USER"),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD"),
        'HOST': os.environ.get("POSTGRES_HOST"),
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
]

AUTH_USER_MODEL = 'client.User'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# CLOUDINARY
USE_CLOUDINARY = False
CLOUDINARY_CLOUD_NAME = ''
CLOUDINARY_API_KEY = ''
CLOUDINARY_API_SECRET = ''

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS SETTINGS
try:
    from .cors_settings import *
except Exception as e:
    print("-" * 100)
    print("Unable to import CORS Settings")
    print("-" * 100)

# LOG SETTINGS
try:
    from .log_settings import *
except Exception as e:
    print("-" * 100)
    print("Unable to import Log Settings")
    print("-" * 100)

# REST FRAMEWORK SETTINGS
try:
    from .rest_framework_settings import *
except Exception as e:
    print("-" * 100)
    print("Unable to import REST Framework Settings")
    print("-" * 100)

# JWT SETTINGS
try:
    from .jwt_settings import *
except Exception as e:
    print("-" * 100)
    print("Unable to import JWT Settings")
    print("-" * 100)

# JAZZMIN SETTINGS
try:
    from .jazzmin_ui_settings import *
except Exception as e:
    print("-" * 60)
    print("Unable to import Jazzmin Settings")
    print(str(e))
    print("-" * 60)

# LOCAL SETTINGS
try:
    from .local_settings import *
except Exception as e:
    print("-" * 100)
    print("Unable to import Local Settings")
    print("-" * 100)

# CLOUDINARY SETTINGS
try:
    from .cloudinary_settings import *
except Exception as e:
    print("-" * 60)
    print("Unable to import Cloudinary Settings")
    print(str(e))
    print("-" * 60)
