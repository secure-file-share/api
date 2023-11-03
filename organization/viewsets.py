from alpha.viewsets import BaseAuthViewSet
from .serializers import OrganizationSerializer


class OrganizationViewSet(BaseAuthViewSet):
    """
    Organization APIs
    """

    def list(self, request):
        try:
            # GET ORGANIZATION DETAIL
            organization_serialized = OrganizationSerializer(
                request.user.organization).data
        except Exception as e:
            print("-" * 100)
            print(
                "Exception caught from 'organization.viewsets.OrganizationViewSet.list'")
            print(str(e))
            print("-" * 100)

            return self.error_response(message="Something went wrong", error=str(e))
        else:
            return self.success_response(data=organization_serialized)
