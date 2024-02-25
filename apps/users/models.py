from datetime import datetime
from typing import List
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from apps.common.models import BaseModel
from apps.common.validators import phone_validator
from apps.common.utils import generate_temp_user_secret, send_email
from apps.users.managers import UserManager


class User(AbstractUser, BaseModel):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    admin_event_position = models.ForeignKey(
        "common.Position",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users",
    )
    private_email = models.EmailField(_("private email address"), null=True, blank=True)
    work_phone_number = models.CharField(
        _("work phone number"),
        max_length=18,
        validators=[phone_validator],
        null=True,
        blank=True,
    )
    telegram = models.URLField(_("telegram"), null=True, blank=True)
    photo = models.ImageField(_("photo"), upload_to="users/")
    job_position = models.CharField(_("position"), max_length=255)
    bio = models.TextField(_("comment"), null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: List[str] = []
    objects = UserManager()

    raw_password = models.CharField(
        max_length=255, null=True, blank=True, editable=False
    )

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def save(self, *args, **kwargs):
        if self._password is not None:
            self.raw_password = self._password
        super().save(*args, **kwargs)

    @property
    def user_position(self):
        return self.admin_event_position if self.admin_event_position else ""

    def __str__(self):
        return f"{self.email}"


class CustomUser(models.Model):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=True)
    country = models.ForeignKey(
        "Country", on_delete=models.PROTECT, verbose_name=_("country")
    )
    password = models.CharField(_("password"), max_length=128)  # hashed password
    secret = models.CharField(
        _("secret"), max_length=128, default=generate_temp_user_secret
    )

    class Meta:
        verbose_name = _("Custom user")
        verbose_name_plural = _("Custom users")

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def send_confirmation_email(self):
        data = {
            "full_name": self.first_name + " " + self.last_name,
            "frontend_confirm_url": settings.FRONTEND_REG_CONFIRM_URL,
            "token": self.token,
            "id": self.id,
        }

        send_email(
            subject="reg_confirm_email_sub",
            user_email=self.email,
            data=data,
            email_template="auth/email_confirm.html",
        )

    def create_user(self) -> User:
        user = User.objects.create_user(
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
            country=self.country,
        )
        user.password = self.password
        user.save()
        return user

    @property
    def token(self):
        return f"{self.id}:{self.secret}"
