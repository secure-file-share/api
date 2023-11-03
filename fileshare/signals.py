import os
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from .models import Files, FileShare


@receiver(models.signals.pre_save, sender=Files)
def create_file_meta(sender, instance, **kwargs):
    """
    Create meta data for file.
    """

    file_name_split = instance.file_instance.url.split("/")[-1].split(".")
    print(file_name_split)

    if len(file_name_split[-1]) < 10:
        instance.ext = file_name_split.pop()

    if not instance.name:
        instance.name = "_".join(file_name_split)

    print(instance.name)
    instance.size = instance.file_instance.size


@receiver(models.signals.post_delete, sender=Files)
def delete_file(sender, instance, **kwargs):
    """
    Delete file after deletion from database.
    """
    if settings.USE_CLOUDINARY:
        # FOR CLOUDINARY
        try:
            instance.file_instance.delete(save=False)
        except:
            pass
    else:
        # FOR LOCALLY SAVED FILES
        try:
            if os.path.isfile(instance.file_instance.path):
                os.remove(instance.file_instance.path)
        except:
            pass


@receiver(models.signals.pre_save, sender=Files)
def update_file(sender, instance, **kwargs):
    """
    Update files after updating from database.
    """

    if not instance.pk:
        return False

    # OLD FILE
    try:
        old_instance = Files.objects.get(pk=instance.pk)
        old_file = old_instance.file_instance
    except Files.DoesNotExist:
        return False

    # NEW FILE
    new_file = instance.file_instance

    # DELETE OLD FILE IF FILE IS UPDATED
    if not old_file == new_file:
        if settings.USE_CLOUDINARY:
            # DELETE FROM CLOUDINARY
            try:
                old_file.delete(save=False)
            except:
                pass
        else:
            # DELETE FROM LOCAL
            try:
                if os.path.isfile(old_file.path):
                    os.remove(old_file.path)
            except:
                pass


@receiver(models.signals.post_delete, sender=FileShare)
def delete_file_share(sender, instance, **kwargs):
    """
    Delete file after deletion of its file share link.
    """

    instance.file_instance.delete()
