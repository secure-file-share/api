from django.db import models
from alpha.extra_models import TimestampWithRecord
from .utilities import get_file_upload_path, get_file_expiration_date, get_unique_code


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

    @property
    def file(self):
        return self.file_instance

    def get_organization_name(self):
        """Return organization name."""

        return self.organization.name


class FileShare(TimestampWithRecord):
    """
    File Share data model

    ---
    file : Files (Django)
    shared_to : User (Django)
    unique_code : Char
    """

    file_instance = models.ForeignKey(
        Files, related_name="share", on_delete=models.CASCADE)
    shared_to = models.ForeignKey(
        "client.User", related_name="shared_files", on_delete=models.CASCADE)
    unique_code = models.CharField(
        max_length=50, default=get_unique_code, help_text="Unique code used for creating sharing links", unique=True)

    class Meta:
        verbose_name = "File Share"
        verbose_name_plural = "File Share"

    def __str__(self):
        return f"{self.file_instance.get_organization_name()} | {self.unique_code}"
