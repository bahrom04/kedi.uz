from django.contrib.auth import get_user_model, login, logout
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from apps.users.auth import serializers
from apps.common.validators import (
    custom_validation,
    validate_email,
    validate_password,
    validate_username,
)


class UserRegisterView(APIView):
    # queryset = User.objects.all()
    # serializer_class = serializers.RegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        validated_data = custom_validation(request.data)
        serializer = serializers.RegistrationSerializer(data=validated_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(validated_data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication]

    def post(self, request):
        data = request.data
        assert validate_email(data)
        assert validate_password(data)
        serializer = serializers.LoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)


class UserLogoutView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class UserDetailView(APIView):
	permission_classes = [IsAuthenticated]
	authentication_classes = [SessionAuthentication]

	def get(self, request):
		serializer = serializers.UserDetailSerializer(request.user)
		return Response({'user': serializer.data}, status=status.HTTP_200_OK)
