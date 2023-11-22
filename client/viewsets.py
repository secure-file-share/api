from django.db.models import Q
from alpha.viewsets import BaseAuthViewSet
from alpha.utilities import parse_request_body
from .models import User
from .serializers import UserSerializer


class ClientUserViewSet(BaseAuthViewSet):
    """
    Client User APIs
    """

    def list(self, request):
        try:
            user_serialized = UserSerializer(request.user).data
        except Exception as e:
            print("-" * 100)
            print("Exception caught from 'client.viewsets.ClientUserViewSet.list'")
            print(str(e))
            print("-" * 100)

            return self.error_response(message="Something went wrong", error=str(e))
        else:
            return self.success_response(data=user_serialized)

    def create(self, request):
        try:
            # UPDATE SELF DATA
            user = request.user

            data = parse_request_body(request)
            first_name = data.get("first_name")
            last_name = data.get("last_name")
            username = data.get("username")
            email = data.get("email")

            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email

            user.save()

            user_serialized = UserSerializer(user).data
        except Exception as e:
            print("-" * 100)
            print("Exception caught from 'client.viewsets.ClientUserViewSet.create'")
            print(str(e))
            print("-" * 100)

            return self.error_response(message="Something went wrong", error=str(e))
        else:
            return self.success_response(data=user_serialized)


class UserViewSet(BaseAuthViewSet):
    """
    User APIs
    """

    def list(self, request):
        try:
            # FOR SEARCH
            query = request.query_params.get("q")
            organization = request.user.organization

            # SEARCH USERS WITHIN ORGANIZATION ONLY
            users = User.objects.filter(
                id__in=organization.users.all().values_list("user", flat=True))

            # SEARCH
            users_searched = users.filter(Q(username=query) | Q(email=query))

            # SERIALIZED
            users_serialized = UserSerializer(users_searched, many=True).data
        except Exception as e:
            print("-" * 100)
            print("Exception caught from 'client.viewsets.UserViewSet.list'")
            print(str(e))
            print("-" * 100)

            return self.error_response(message="Something went wrong", error=str(e))
        else:
            return self.success_response(data=users_serialized)
