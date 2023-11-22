import os
import pytz
from random import randint
from uuid import UUID
from django.conf import settings
from datetime import datetime, timedelta
# from alpha.utilities import random_string


def get_file_upload_path(instance, filename):
    """Returns path to upload files."""

    path = "prod"
    if settings.DEBUG:
        path = "dev"

    return os.path.join("files", path, f"{instance.name} [{str(instance.id)}]", "original", filename)


def get_file_expiration_date():
    """Returns datetime instance of 1 week from now"""
    return datetime.now().astimezone(pytz.timezone(settings.TIME_ZONE)) + timedelta(days=7)


def get_unique_code():
    # """Returns random string of 50 length."""
    # return random_string(length=50)

    # SO USERS CAN USE THIS CODE TO RETRIEVE FILE AS WELL
    """Returns random 6 digit code."""
    return randint(100000, 999999)


def is_valid_uuid(uuid_to_test, version=4):
    """
    Check if uuid_to_test is a valid UUID.
    """

    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test
