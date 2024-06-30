from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common import models as common

class Community(common.BaseModel):
    title = models.CharField(_("Title"), max_length=128)
    image = models.ImageField(upload_to="community/")

    description = models.TextField(_("Description"), blank=True, null=True)  # Add this line


    telegram_link = models.URLField()
