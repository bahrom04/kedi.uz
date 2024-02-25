from django.conf import settings
from rest_framework.exceptions import ValidationError
from rest_framework.fields import EmailField
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from common import models
from common.auth import serializers
from common.generics import MutateView


class RegistrationView(MutateView):
    serializer_class = serializers.RegistrationSerializer

    def perform_mutate(self, serializer):
        instance: models.TempUser = serializer.save()
        if settings.EMAIL_WORKING:
            instance.send_confirmation_email()


class RegistrationVerifyView(MutateView):
    serializer_class = serializers.RegistrationVerifySerializer


class CheckAccountView(APIView):
    """
    Check if an account exists with the given email.
    Query params:
        email: str
    """

    def get(self, request, *args, **kwargs):
        email = request.GET.get("email")
        try:
            EmailField().run_validation(email)
        except ValidationError as e:
            return Response({"email": e.detail}, status=400)

        if models.User.objects.filter(email=email).exists():
            return Response({"exists": True})
        return Response({"exists": False})


class PasswordResetView(MutateView):
    serializer_class = serializers.PasswordResetSerializer

    def perform_mutate(self, serializer):
        serializer.save()
        session = serializer.validated_data["verification"]["session"]
        session.expire()


class LoginView(TokenObtainPairView):
    throttle_scope = "login"
