from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from apps.common import models as common

class Community(common.BaseModel):
    image = models.ImageField(upload_to="community/")
    title = models.CharField(_("Title"), max_length=128)
    description = models.TextField(_("Description"), blank=True, null=True)

    telegram_link = models.URLField()


class LostPet(common.BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=32)
    # status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)