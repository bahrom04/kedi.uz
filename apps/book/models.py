from django.db import models
from apps.common import models as common


class Community(common.BaseModel):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="community/")

    telegram_link = models.URLField()
