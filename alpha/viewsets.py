from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from .responses import success_response, error_response


class BaseAuthViewSet(GenericViewSet):
    """Base Authenticated View Set."""

    status = status

    class Meta:
        abstract = True

    def success_response(self, data=None, message=None, error=None, status=status.HTTP_200_OK):
        return success_response(data, message, error, status)

    def error_response(self, data=None, message=None, error=None, status=status.HTTP_500_INTERNAL_SERVER_ERROR):
        return error_response(data=data, message=message, error=error, status=status)


class BaseViewSet(GenericViewSet):
    """Base Unauthenticated View Set."""

    status = status
    permission_classes = [AllowAny]

    class Meta:
        abstract = True

    def success_response(self, data=None, message=None, error=None, status=status.HTTP_200_OK):
        return success_response(data, message, error, status)

    def error_response(self, data=None, message=None, error=None, status=status.HTTP_500_INTERNAL_SERVER_ERROR):
        return error_response(data=data, message=message, error=error, status=status)
