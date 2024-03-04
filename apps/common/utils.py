from django.conf import settings
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from apps.users.models import User
from random import randint


REG_CONFIRM_EMAIL_SUB = _("Ekologiya: New user registration confirmation")
RESPONSE_RECEIVED = _("Response received from the Ekologiya")


def send_confirmation_email(email):
    otp = randint(1000, 9999)
    email_from = settings.EMAIL_HOST_USER
    send_mail(
        subject=REG_CONFIRM_EMAIL_SUB,
        from_email=email_from,
        recipient_list=[email],
        message=f"your verify code: {otp}",
    )
    user = User.objects.get(email=email)
    user.otp = otp
    user.save()
