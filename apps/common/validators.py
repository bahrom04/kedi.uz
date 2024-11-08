import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# from rest_framework import serializers
# # from django.contrib.auth import get_user_model
# from apps.users import models


# # UserModel = get_user_model()


# def custom_validation(data):
#     email = data["email"].strip()
#     username = data["username"].strip()
#     password = data["password"].strip()
#     ##
#     if not email or models.User.objects.filter(email=email).exists():
#         raise ValidationError("choose another email")
#     ##
#     if not password or len(password) < 8:
#         raise ValidationError("choose another password, min 8 characters")
#     ##
#     if not username:
#         raise ValidationError("choose another username")
#     return data


# def validate_email(data):
#     email = data["email"].strip()
#     if not email:
#         raise ValidationError("Email is needed")
#     return True


# def validate_username(data):
#     username = data["username"].strip()
#     if not username:
#         raise ValidationError("choose another username")
#     return True


# def validate_password(data):
#     password = data["password"].strip()
#     if not password:
#         raise ValidationError("a password is needed")
#     return True


def phone_validator(phone):
    regex = r"^(\+?998)?[0-9]{9}$"
    if not re.match(regex, phone):
        raise ValidationError(_("Phone number is not valid"), code="invalid")


# ALLOWED_UPLOAD_EXTENSIONS = [
#     # images
#     ".jpg",
#     ".jpeg",
#     ".png",
#     ".gif",
#     ".svg",
#     # documents
#     ".pdf",
#     ".xls",
#     ".xlsx",
# ]
