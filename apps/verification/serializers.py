from django.core.exceptions import ValidationError as DjangoValidationError
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.serializers import ValidationError

from common.validators import phone_validator
from verification.helpers import VerificationHelper
from verification.models import VerificationSession


class RequestOTPSerializer(serializers.ModelSerializer):
    address = serializers.CharField(max_length=255)

    class Meta:
        model = VerificationSession
        fields = ["type", "address", "purpose", "client_secret"]

    def validate_address(self, value):
        if self.initial_data["type"] == VerificationSession.Types.EMAIL:
            try:
                EmailValidator()(value)
            except DjangoValidationError:
                raise ValidationError(_("enter a valid email address"), code="invalid_email_address")
        elif self.initial_data["type"] == VerificationSession.Types.PHONE:
            try:
                phone_validator(value)
            except DjangoValidationError:
                raise ValidationError(_("enter a valid phone number"), code="invalid_phone_address")
        return value

    def create(self, validated_data):
        return VerificationHelper.get_or_create_session(
            validated_data["type"],
            validated_data["purpose"],
            validated_data["address"],
            validated_data["client_secret"],
        )

    def to_representation(self, instance):
        return {
            "sid": instance.id,
            "wait": 60,
        }


class SubmitOTPSerializer(serializers.ModelSerializer):
    sid = serializers.IntegerField(source="id")

    class Meta:
        model = VerificationSession
        fields = ["sid", "otp", "client_secret"]

    def create(self, validated_data):
        try:
            return VerificationHelper.validate_session(
                validated_data["id"], validated_data["client_secret"], validated_data["otp"]
            )
        except VerificationHelper.InvalidOTPError:
            raise serializers.ValidationError({"otp": [_("Invalid OTP")]}, code="invalid_otp")
        except VerificationHelper.TooManyInvalidOTPError:
            raise serializers.ValidationError(
                {"non_field_errors": [_("Too many invalid attempts. Please request a new OTP")]},
                code="too_many_invalid_attempts",
            )
        except VerificationHelper.SessionNotFoundError:
            raise serializers.ValidationError(
                {"non_field_errors": [_("Session not found or expired")]}, code="session_not_found"
            )

    def to_representation(self, instance):
        return {
            "sid": instance.id,
            "validated": instance.validated,
        }


class VerificationSerializer(serializers.Serializer):
    sid = serializers.IntegerField()
    client_secret = serializers.CharField(max_length=32)

    def validate(self, attrs):
        sid = attrs.get("sid")
        client_secret = attrs.get("client_secret")
        try:
            session = VerificationHelper.get_validated_session(sid, client_secret)
        except VerificationHelper.SessionNotFoundError:
            raise ValidationError(_("Session not found or expired"), code="session_not_found")
        attrs["session"] = session
        return attrs
