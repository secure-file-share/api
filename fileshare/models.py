from django.db import models
from alpha.extra_models import TimestampWithRecord
from .utilities import get_file_upload_path, get_file_expiration_date


class Files(TimestampWithRecord):
    """
    Files

    ---
    name : Char
    ext : Char
    size : Float
    file : File
    organization : Organization (Django)
    uploaded_by : User (Django)
    expiration : DateTime
    """

    # FILE INFO
    name = models.CharField(
        max_length=200, help_text="File Name (Do not enter file extension here)", blank=True)
    ext = models.CharField(
        max_length=10, help_text="File Extension", blank=True)
    size = models.FloatField(default=0, blank=True)

    # FILE
    file_instance = models.FileField(
        upload_to=get_file_upload_path, max_length=1000, verbose_name="File", help_text="Upload the file here", null=True)
    expiration = models.DateTimeField(
        verbose_name="File expiration", help_text="Files will be deleted after this date.", blank=True, default=get_file_expiration_date)

    # ORGANIZATION
    organization = models.ForeignKey(
        "organization.Organization", related_name="files", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Files"
        verbose_name_plural = "Files"

    def __str__(self):
        if self.name:
            return self.name

        return f"File instance of {self.organization.name}"
