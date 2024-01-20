import os
import sys
from django.core.management.base import BaseCommand  # , CommandError
from client.models import User


class Command(BaseCommand):
    help = 'Create admin user'

    def handle(self, *args, **options):
        try:
            user, created = User.objects.get_or_create(username="admin")

            user.active = True
            user.is_staff = True
            user.is_superuser = True

            user.set_password(os.environ.get(
                "ADMIN_USER_PASSWORD", 'strongpassword'))
            user.save()
        except Exception as e:
            print(e)
            sys.stdout.flush()
