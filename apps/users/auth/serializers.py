from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from users import models
from verification.serializers import VerificationSerializer


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ["id", "first_name", "last_name", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_email(self, value):
        if models.User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                _("User with this email already exists"), code="email_exists"
            )
        return value

    def validate(self, attrs):
        password = attrs.pop("password")
        temp_user = models.CustomUser(**attrs)
        try:
            validate_password(password, user=temp_user)
        except serializers.DjangoValidationError as e:
            raise serializers.ValidationError(
                {"password": serializers.as_serializer_error(e)["non_field_errors"]}
            )

        attrs["password"] = password
        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = models.CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user


class RegistrationVerifySerializer(serializers.Serializer):
    token = serializers.CharField()

    @staticmethod
    def validate_token(value):
        """
        token is in format of id:secret for a CustomUser instance
        """

        try:
            id, secret = value.split(":")
            temp_user = models.CustomUser.objects.get(id=id, secret=secret)
        except ValueError:
            raise serializers.ValidationError(_("Invalid token"), code="invalid_token")
        except models.CustomUser.DoesNotExist:
            raise serializers.ValidationError(_("Invalid token"), code="invalid_token")

        # check if email is in use
        if models.User.objects.filter(email=temp_user.email).exists():
            raise serializers.ValidationError(
                _("Token is expired"), code="expired_token"
            )

        return temp_user

    def create(self, validated_data):
        with transaction.atomic():
            temp_user: models.CustomUser = validated_data["token"]
            user = temp_user.create_user()
        return user


class PasswordResetSerializer(serializers.Serializer):
    verification = VerificationSerializer()
    password = serializers.CharField()

    def validate_password(self, value):
        try:
            validate_password(value)
        except serializers.DjangoValidationError as e:
            raise serializers.ValidationError(
                serializers.as_serializer_error(e)["non_field_errors"]
            )
        return value

    def create(self, validated_data):
        session = validated_data["verification"]["session"]
        password = validated_data["password"]

        try:
            user = models.User.objects.get(email=session.address)
        except models.User.DoesNotExist:
            raise serializers.ValidationError(
                _("User does not exist"), code="user_not_found"
            )
        user.set_password(password)
        user.save()
        return user

   
