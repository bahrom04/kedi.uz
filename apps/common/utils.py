import datetime
import os
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string

REG_CONFIRM_EMAIL_SUB = _("Ekologiya: New user registration confirmation")
RESPONSE_RECEIVED = _("Response received from the Ekologiya")


def send_email(subject: str, user_email: str, data: dict, email_template: str):
    subject_choices = {
        "reg_confirm_email_sub": REG_CONFIRM_EMAIL_SUB,
        "response_received": RESPONSE_RECEIVED,
    }

    # separating the timezone into date and time
    formatted_date = timezone.now().strftime("%d.%m.%Y")
    formatted_time = timezone.now().strftime("%H:%M:%S")

    data["date"] = formatted_date
    data["time"] = formatted_time

    msg_html = render_to_string(email_template, context=data)
    message = EmailMultiAlternatives(
        subject=subject_choices[subject],
        from_email=settings.EMAIL_HOST_USER,
        to=[user_email],
    )
    message.attach_alternative(msg_html, "text/html")
    message.send(fail_silently=False)


def generate_temp_user_secret():
    """
    Generate a random string to be used as a temporary user secret.
    """
    return get_random_string(length=32)
