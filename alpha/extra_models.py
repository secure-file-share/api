from uuid import uuid4
from django.db import models
from threadlocals.threadlocals import get_current_request  # , get_current_user
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AnonymousUser


class Timestamp(models.Model):
    """
    Timestamp abstract model to record time history of data.

    ---
    Fields

    id : UUID
    created_at : DateTime
    updated_at : DateTime
    """
    id = models.UUIDField(primary_key=True, default=uuid4,
                          unique=True, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    @property
    def primary_key(self):
        return str(self.id)


class Record(models.Model):
    """
    Abstract model to record changes history of data.

    ---
    Fields

    created_by : User (Django)
    updated_by : User (Django)
    """

    created_by = models.ForeignKey('client.User', verbose_name=_(
        "Created By"), related_name="%(app_label)s_%(class)s_created", on_delete=models.DO_NOTHING, editable=False, null=True)
    updated_by = models.ForeignKey('client.User', verbose_name=_(
        "Updated By"), related_name="%(app_label)s_%(class)s_updated", on_delete=models.DO_NOTHING, editable=False, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        request = get_current_request()

        # PROCEED IF ONLY THERE IS A VALID REQUEST THREAD
        if request:
            user = request.user

            # DO NOT UPDATE updated_by IF THE USER OBJECT IS AnonymousUser
            if request and not isinstance(user, AnonymousUser):
                self.updated_by = user

                try:
                    if not self.created_by:
                        self.created_by = user
                except:
                    self.created_by = user

        return super().save(*args, **kwargs)


class TimestampWithRecord(Timestamp, Record):
    """Abstract model combined with Timestamp and Record models."""
    class Meta:
        abstract = True
