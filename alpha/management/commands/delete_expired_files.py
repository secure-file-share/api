import sys
import pytz
from datetime import datetime
from django.conf import settings
from django.core.management.base import BaseCommand  # , CommandError
from fileshare.models import Files
from alpha.utilities import parse_date


class Command(BaseCommand):
    help = 'Delete expired files.'

    def handle(self, *args, **options):
        now = datetime.now().astimezone(pytz.timezone(settings.TIME_ZONE))

        expired_files = Files.objects.filter(expiration__lte=now)

        sys.stdout.flush()
        print("-" * 100)
        print("Delete expired files.")
        print("Files to be deleted before expiration date =",
              parse_date(now, format="%b. %m, %Y %H:%M:%S"))
        print("-" * 100)
        print(expired_files.count(), "expired files found.")
        sys.stdout.flush()

        counter = 0
        for file_ in expired_files:
            print("-" * 100)
            print("Deleting file", file_.name)
            print("Organization:", file_.get_organization_name())
            print("-" * 100)
            sys.stdout.flush()

            try:
                file_.delete()
            except Exception as e:
                print("Unable to delete.")
                print(str(e))
            else:
                print("Deleted")
                counter += 1

            sys.stdout.flush()

        print("-" * 100)
        print(counter, "expired files deleted.")
        print("-" * 100)
        sys.stdout.flush()
