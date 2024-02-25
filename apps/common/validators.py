from django.core.exceptions import ValidationError
import re


def phone_validator(phone):
    regex = r"^(\+?998)?[0-9]{9}$"
    if not re.match(regex, phone):
        raise ValidationError(_("Phone number is not valid"), code="invalid")


ALLOWED_UPLOAD_EXTENSIONS = [
    # images
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".svg",
    # documents
    ".pdf",
    ".xls",
    ".xlsx",
]
