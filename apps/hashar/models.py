from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor_uploader.fields import RichTextUploadingField
from apps.common import models as common


# Create your models here.
class HasharDetail(common.BaseModel):
    title = models.CharField(max_length=255)
    description = RichTextUploadingField()

    location = models.CharField(max_length=255)
    latitude = models.DecimalField(
        max_digits=32,
        decimal_places=6,
        validators=[MinValueValidator(-90), MaxValueValidator(90)],
        blank=True,
        null=True,
    )
    longitude = models.DecimalField(
        max_digits=32,
        decimal_places=6,
        validators=[MinValueValidator(-180), MaxValueValidator(180)],
        blank=True,
        null=True,
    )

    media = models.ForeignKey("common.Media", related_name="hashar_detail")

    event = models.ForeignKey("common.Event", on_delete=models.CASCADE)
