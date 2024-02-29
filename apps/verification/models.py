from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _

from verification.templates import VERIFICATION_EMAIL_TEMPLATES


class VerificationSession(models.Model):
    class Types(models.TextChoices):
        EMAIL = "email", _("Email")
        PHONE = "phone", _("Phone")

    class Purposes(models.TextChoices):
        RESET_PASSWORD = "reset_password", _("Reset password")

    type = models.CharField(choices=Types.choices, max_length=5)
    address = models.CharField(max_length=255)
    client_secret = models.CharField(max_length=32)
    otp = models.CharField(max_length=32)
    invalid_attempts = models.PositiveIntegerField(default=0)
    purpose = models.CharField(max_length=64, choices=Purposes.choices)
    validated = models.BooleanField(default=False)
    expired = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    validated_at = models.DateTimeField(null=True, blank=True)

    def send_otp(self):
        if self.type == self.Types.PHONE:
            self._send_phone_otp()
        elif self.type == self.Types.EMAIL:
            self._send_email_otp()
        else:
            raise Exception("Unknown type")

    def _send_email_otp(self):
        template = VERIFICATION_EMAIL_TEMPLATES[self.purpose]
        subject = self.get_purpose_display()
        message = template.format(otp=self.otp)
        send_mail(subject, message, settings.EMAIL_HOST_USER, [self.address], fail_silently=False)

    def _send_phone_otp(self, **kwargs):
        raise NotImplementedError()

    def expire(self):
        self.expired = True
        self.save(update_fields=["expired"])

    class Meta:
        verbose_name = _("verification session")
        verbose_name_plural = _("verification sessions")