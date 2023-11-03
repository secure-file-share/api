from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from client.models import User
from client.serializers import UserSerializer
from alpha.responses import send_with_cors


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        return token


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")

            user = User.objects.get(username=username)

            if not user.check_password(password):
                raise Exception(
                    f"Wrong password: user={username};pass={password}")
        except Exception as e:
            print("-" * 100)
            print(
                f"Exception from 'securefileshare.CustomTokenObtainPairView.post':\n{str(e)}")
            print("-" * 100)
            response = Response(
                {"message": "Unable to authenticate"}, status=status.HTTP_401_UNAUTHORIZED)
            return send_with_cors(response)
        else:
            response = super().post(request)
            response.data["user"] = UserSerializer(user).data
            return response
