from corsheaders.defaults import default_headers

try:
    from . import local_settings
    django_debug = local_settings.DEBUG
except:
    from django.conf import settings
    django_debug = settings.DEBUG


# if django_debug:
#     CORS_ORIGIN_ALLOW_ALL = True
# else:
#     CORS_ORIGIN_ALLOW_ALL = False
#     CORS_ALLOWED_ORIGINS = []


CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = list(default_headers)
CORS_ALLOW_HEADERS.extend([])
