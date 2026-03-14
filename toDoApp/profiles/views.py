from tokenize import TokenError

from django.contrib.auth import get_user_model, authenticate
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from toDoApp.profiles.serializers import UserModelSerializer


UserModel = get_user_model()


class RegisterView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = (AllowAny, )


class LoginView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({
                "error": "Invalid username or password",
            },
                status=status.HTTP_401_UNAUTHORIZED,
        )

        refresh = RefreshToken.for_user(user)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "message": "Login successful",
        },
            status=status.HTTP_200_OK,
        )


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh = request.data.get("refresh")
            token = RefreshToken(refresh)
            token.blacklist()
            return Response({
                "message": "Logged out successfully",
            },
                status=status.HTTP_200_OK
            )
        except TokenError:
            return Response({
                "error": "Invalid token",
            },
                status=status.HTTP_400_BAD_REQUEST,
            )