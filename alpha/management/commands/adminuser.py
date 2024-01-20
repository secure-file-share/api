import os
from django.core.management.base import BaseCommand  # , CommandError
from client.models import User


class Command(BaseCommand):
    help = 'Create admin user'

    def handle(self, *args, **options):
        user = User.objects.create(username="admin")

        user.active = True
        user.is_staff = True
        user.is_superuser = True

        user.set_password(os.environ.get(
            "ADMIN_USER_PASSWORD", 'strongpassword'))
        user.save()
