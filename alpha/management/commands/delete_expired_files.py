import os
import sys
import pytz
from datetime import datetime
from django.conf import settings
from django.core.management.base import BaseCommand  # , CommandError
from fileshare.models import Files
from alpha.utilities import parse_date


class Command(BaseCommand):
    help = 'Delete expired and temporary files.'

    def handle(self, *args, **options):
        now = datetime.now().astimezone(pytz.timezone(settings.TIME_ZONE))

        expired_files = Files.objects.filter(expiration__lte=now)
        temp_files = settings.BASE_DIR / "temp"

        sys.stdout.flush()
        print("-" * 100)
        print("Delete expired and temporary files.")
        print("Files to be deleted before expiration date =",
              parse_date(now, format="%b. %m, %Y %H:%M:%S"))
        print("-" * 100)
        print(expired_files.count(), "expired files found.")
        print("-" * 100)
        print(len(os.listdir(temp_files)), "temporary files found")
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
        sys.stdout.flush()

        counter = 0
        (dirpath, dirnames, filenames) = next(os.walk(temp_files))

        for file_ in filenames:
            print("-" * 100)
            print("Deleting file", file_)
            print("-" * 100)
            sys.stdout.flush()

            try:
                os.remove(os.path.join(dirpath, file_))
            except Exception as e:
                print("Unable to delete.")
                print(str(e))
            else:
                print("Deleted")
                counter += 1

            sys.stdout.flush()

        print("-" * 100)
        print(counter, "temporary files deleted.")
        print("-" * 100)
        sys.stdout.flush()
