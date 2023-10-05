from rest_framework import serializers
from .utilities import parse_date


class BaseSerializer(serializers.ModelSerializer):
    """Base Serializers for generally all models."""

    created_at = serializers.SerializerMethodField("get_created_at")
    created_by = serializers.SerializerMethodField("get_created_by")
    updated_at = serializers.SerializerMethodField("get_updated_at")
    updated_by = serializers.SerializerMethodField("get_updated_by")

    class Meta:
        abstract = True
        # fields = (
        #     "created_at",
        #     "created_by",
        #     "updated_at",
        #     "updated_by"
        # )

    def get_created_at(self, value):
        try:
            timestamp = value.created_at.timestamp()
        except:
            timestamp = None

        try:
            datetime = parse_date(
                value.created_at, format="%b. %d %Y, %H:%M:%S")
        except:
            datetime = None

        return {
            "timestamp": timestamp,
            "datetime": datetime
        }

    def get_created_by(self, value):
        if value.created_by:
            return {
                "id": str(value.created_by.id),
                "username": value.created_by.username,
                "email": value.created_by.email
            }

        return None

    def get_updated_at(self, value):
        try:
            timestamp = value.updated_at.timestamp()
        except:
            timestamp = None

        try:
            datetime = parse_date(
                value.updated_at, format="%b. %d %Y, %H:%M:%S")
        except:
            datetime = None

        return {
            "timestamp": timestamp,
            "datetime": datetime
        }

    def get_updated_by(self, value):
        if value.updated_by:
            return {
                "id": str(value.updated_by.id),
                "username": value.updated_by.username,
                "email": value.updated_by.email,
            }

        return None
