import os
import pytz
from datetime import datetime, timedelta
from django.conf import settings


def get_file_upload_path(instance, filename):
    """Returns path to upload files."""

    path = "prod"
    if settings.DEBUG:
        path = "dev"

    return os.path.join("files", path, f"{instance.name} [{str(instance.id)}]", "original", filename)


def get_file_expiration_date():
    """Returns datetime instance of 1 week from now"""
    return datetime.now().astimezone(pytz.timezone(settings.TIME_ZONE)) + timedelta(days=7)
