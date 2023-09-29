from django.conf import settings

# DJANGO SETTINGS
DEBUG = True
settings.STAGING = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# DOMAIN NAME WHERE THIS APP INSTANCE WILL BE HOSTED
ALLOWED_HOSTS = []
CSRF_TRUSTED_ORIGINS = ['https://*.YOUR_DOMAIN.COM']
SELF_HOST = ""

# CLOUDINARY
settings.USE_CLOUDINARY = False
settings.CLOUDINARY_CLOUD_NAME = ''
settings.CLOUDINARY_API_KEY = ''
settings.CLOUDINARY_API_SECRET = ''

## OVERWRITE IF REQUIRED! ##
# CORS SETTINGS
# CORS_ORIGIN_ALLOW_ALL = False
# CORS_ALLOWED_ORIGINS = []
