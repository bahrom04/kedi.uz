from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from apps.users import models
from django.contrib.auth import authenticate


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = models.User.objects.create_user(
            email=validated_data["email"], password=validated_data["password"]
        )
        user.username = validated_data["username"]
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def check_user(self, validated_data):
        user = authenticate(
            username=validated_data["email"], password=validated_data["password"]
        )
        if not user:
            raise ValidationError("User not found")
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.User
        fields = ["email", "username"]


# class RegistrationVerifySerializer(serializers.Serializer):
#     token = serializers.CharField()

#     @staticmethod
#     def validate_token(value):
#         """
#         token is in format of id:secret for a CustomUser instance
#         """

#         try:
#             user = models.User.objects.get(id=id)
#         except ValueError:
#             raise serializers.ValidationError(_("Invalid token"), code="invalid_token")
#         except models.User.DoesNotExist:
#             raise serializers.ValidationError(_("Invalid token"), code="invalid_token")

#         # check if email is in use
#         if models.User.objects.filter(email=user.email).exists():
#             raise serializers.ValidationError(
#                 _("Token is expired"), code="expired_token"
#             )

#         return user

#     def create(self, validated_data):
#         with transaction.atomic():
#             user: models.User = validated_data["token"]
#             user = user.create_user()
#         return user
