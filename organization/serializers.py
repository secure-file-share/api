from rest_framework import serializers
from alpha.serializers import BaseSerializer
from .models import Organization


class OrganizationSerializer(BaseSerializer):
    """
    Organization Serializer
    """

    address = serializers.SerializerMethodField("get_address")

    class Meta:
        model = Organization
        fields = (
            "id",
            "name",
            "phone",
            # "secret_code",
            "address",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
        )

    def get_address(self, obj):
        return {
            "street1": obj.address_street1,
            "street2": obj.address_street2,
            "city": obj.address_city,
            "state": obj.address_state,
            "country": obj.address_country,
            "zip": obj.address_zip,
        }
