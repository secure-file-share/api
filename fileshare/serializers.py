from django.urls import reverse
from rest_framework import serializers
from alpha.serializers import BaseSerializer
from .models import Files, FileShare


class FileSerializer(BaseSerializer):
    """File Serializer"""

    size = serializers.SerializerMethodField("get_size")
    shares = serializers.SerializerMethodField("get_shares")
    organization = serializers.SerializerMethodField("get_organization")
    uploaded_by = serializers.SerializerMethodField("get_uploaded_by")

    class Meta:
        model = Files
        fields = (
            "id",
            "name",
            "ext",
            "size",
            "file",
            "shares",
            "organization",
            "uploaded_by",
            "expiration",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by"
        )

    def get_size(self, obj):
        return {
            "bytes": obj.size,
            "megabytes": float("{:0.2f}".format(obj.size/1024))
        }

    def get_shares(self, obj):
        return [
            {
                "id": str(share.id),
                "shared_by": {
                    "id": str(share.created_by.id),
                    "username": share.created_by.username
                },
                "shared_to": {
                    "id": str(share.shared_to.id),
                    "username": share.shared_to.username
                },
                "unique_code": share.unique_code
            }
            for share in obj.share.all()]

    def get_organization(self, obj):
        return {
            "id": str(obj.organization.id),
            "name": obj.organization.name
        }

    def get_uploaded_by(self, obj):
        return {
            "id": str(obj.uploaded_by.id),
            "username": obj.uploaded_by.username,
            "fullname": obj.uploaded_by.full_name
        }


class FileShareSerializer(BaseSerializer):
    """
    File Share Serializer.
    """

    file = serializers.SerializerMethodField("get_file")
    shared_to = serializers.SerializerMethodField("get_shared_to")
    shared_by = serializers.SerializerMethodField("get_shared_by")
    share_link = serializers.SerializerMethodField("get_share_link")

    class Meta:
        model = FileShare
        fields = (
            "id",
            "file",
            "shared_to",
            "shared_by",
            "unique_code",
            "share_link",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by"
        )

    def get_file(self, obj):
        return FileSerializer(obj.file).data

    def get_shared_by(self, obj):
        return {
            "id": str(obj.shared_by.id),
            "username": obj.shared_by.username,
            "fullname": obj.shared_by.full_name
        }

    def get_shared_to(self, obj):
        return {
            "id": str(obj.shared_to.id),
            "username": obj.shared_to.username,
            "fullname": obj.shared_to.full_name
        }

    def get_share_link(self, obj):
        return reverse("fileshare:fileshare-list") + "{}/".format(obj.id)
