from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import BaseModel
from apps.common.validators import phone_validator
from apps.users.managers import UserManager


class User(AbstractUser, PermissionsMixin, BaseModel):
    email = models.EmailField(_("email address"), unique=True)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, blank=True, null=True)

    phone_number = models.CharField(
        _("phone number"),
        max_length=18,
        validators=[phone_validator],
        null=True,
        blank=True,
    )
    telegram = models.URLField(_("telegram"), null=True, blank=True)
    avatar = models.ImageField(_("avatar"), upload_to="users/", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  # type: ignore

    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return f"{self.email}"
