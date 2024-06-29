from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common import models as common

from ckeditor_uploader.fields import RichTextUploadingField


class Community(common.BaseModel):
    title = models.CharField(_("Title"), max_length=255)
    image = models.ImageField(upload_to="community/")

    description = RichTextUploadingField(_("Description"))

    telegram_link = models.URLField()
