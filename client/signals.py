from django.db import models
from django.dispatch import receiver
from .models import User, UserMeta


@receiver(models.signals.post_save, sender=User)
def create_user_meta(sender, instance, **kwargs):
    """
    Create meta data for user.
    """

    if kwargs.get("created"):
        UserMeta.objects.get_or_create(user=instance)
