from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from alpha.extra_models import Timestamp


class User(AbstractUser):
    """User"""

    id = models.UUIDField(primary_key=True, default=uuid4,
                          unique=True, editable=False)

    objects = UserManager()

    class Meta:
        ordering = ["-date_joined"]

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        """Get Full Name."""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        elif self.username:
            return self.username

        return ""


class UserMeta(Timestamp):
    """Meta data of users"""

    user = models.OneToOneField(
        User, related_name="meta", on_delete=models.CASCADE)
    level = models.PositiveIntegerField()
    organization = models.ForeignKey(
        "organization.Organization", related_name="users", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "User Meta"
        verbose_name_plural = "User Meta"

    def __str__(self):
        return f"{self.user.username} | Meta data"
