from rest_framework import serializers
from alpha.serializers import BaseSerializer
from alpha.utilities import parse_date, relative_date
from .models import User  # , UserMeta


class UserSerializer(BaseSerializer):
    """
    Client User Serializer
    """

    last_login = serializers.SerializerMethodField("get_last_login")
    level = serializers.SerializerMethodField("get_level")
    organization = serializers.SerializerMethodField("get_organization")

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "last_login",
            "is_staff",
            "is_superuser",
            "is_active",
            "level",
            "organization"
        )

    def get_last_login(self, obj):
        if obj.last_login:
            return {
                "datetime": parse_date(obj.last_login),
                "relative": relative_date(obj.last_login),
                "timestamp": obj.last_login.timestamp(),
            }
        else:
            return {
                "datetime": None,
                "relative": None,
                "timestamp": None,
            }

    def get_level(self, obj):
        return {
            "value": obj.meta.level,
            "display": obj.meta.get_level_display()
        }

    def get_organization(self, obj):
        return {
            "id": str(obj.meta.organization.id),
            "name": obj.meta.organization.name,
        }
