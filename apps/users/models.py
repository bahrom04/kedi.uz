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
    # username = None
    email = models.EmailField(_("email address"), unique=True)

    work_phone_number = models.CharField(
        _("work phone number"),
        max_length=18,
        validators=[phone_validator],
        null=True,
        blank=True,
    )
    telegram = models.URLField(_("telegram"), null=True, blank=True)
    avator = models.ImageField(_("avatar"), upload_to="users/")
    bio = models.TextField(_("comment"), null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: List[str] = []
    objects = UserManager()

    password = models.CharField(max_length=255, null=True, blank=True, editable=False)

    def create_user(self):
        user = User.objects.create_user(
            email=self.email,
            first_name=self.first_name,
            last_name=self.last_name,
        )
        user.password = self.password
        user.save()
        return user

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

    @property
    def token(self):
        return f"{self.id}:{self.secret}"

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return f"{self.email}"
