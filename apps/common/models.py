from datetime import datetime
from typing import List
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

from django.contrib.auth.models import UserManager as DjangoUserManager
from django.core.exceptions import ValidationError
from ckeditor_uploader.fields import RichTextUploadingField
from location_field.models.plain import PlainLocationField
from ckeditor_uploader.fields import RichTextUploadingField



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        try:
            return self.title
        except:
            return str(self.id)


class Media(BaseModel):
    class MediaType(models.TextChoices):
        VIDEO = "video", _("Video")
        IMAGE = "image", _("Image")

    file = models.FileField(_("File"), upload_to="uploads/%Y/%m/%d/")
    file_type = models.CharField(
        _("File Type"), choices=MediaType.choices, max_length=255
    )
    position = models.ForeignKey("common.Position", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Media")




class Region(models.Model):
    class RegionType(models.TextChoices):
        TASHKENT_CITY = "Tashkent City", _("Tashkent City")
        TASHKENT_REGION = "Tashkent Region", _("Tashkent Region")
        ANDIJAN = "Andijan", _("Andijan Region")
        NAMANGAN = "Namangan", _("Namangan Region")
        FERGANA = "Fergana", _("Fergana Region")
        SIRDARYA = "Sirdarya", _("Sirdarya Region")
        JIZZAH = "Jizzah", _("Jizzah Region")
        SAMARQAND = "Samarqand", _("Samarqand Region")
        QASHQADARYA = "Qashqadarya", _("Qashqadarya Region")
        SURKHANDARYA = "Surkhandarya", _("Surkhandarya Region")
        BUKHARA = "Bukhara", _("Bukhara Region")
        NAVOI = "Navoi", _("Navoi Region")
        XORAZM = "Xorazm", _("Xorazm Region")
        KARAQALPAK_REPUBLIC = "Karakalpak Republik", _("Karakalpak Republik")

    type = models.CharField(
        _("Street name (Arentir)"),
        choices=RegionType.choices,
        default=RegionType.TASHKENT_CITY,
        max_length=255,
        unique=True,
    )

    def __str__(self):
        return self.type

    class Meta:
        db_table = "Region"
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")


class Blog(BaseModel):
    title = models.CharField(_("Title"), max_length=255)
    thumbnail = models.ForeignKey(
        Media,
        on_delete=models.CASCADE,
        related_name="blogs",
        verbose_name=_("Thumbnail image"),
    )
    description = RichTextUploadingField(_("Description"))

    class Meta:
        db_table = "Blog"
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")
        ordering = ("title",)


class Event(BaseModel):
    class EventType(models.TextChoices):
        HASHAR = "Hashar", _("Hashar")
        ANIMALS_FEEDING = "Animals Feeding", _("Animals Feeding")

    is_active = models.BooleanField(_("Is active"), default=True)
    title = models.CharField(
        _("Event Type"),
        choices=EventType.choices,
        default=EventType.HASHAR,
        max_length=255,
        unique=True,
    )

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")


class Position(BaseModel):
    title = models.CharField(max_length=255)
    description = RichTextUploadingField()

    location = PlainLocationField(
        based_fields=["city"], zoom=10, default="41.311151,69.279737"
    )
    latitude = models.FloatField(verbose_name=_("latitude"), null=True, blank=True)
    longitude = models.FloatField(verbose_name=_("longitude"), null=True, blank=True)

    start_time = models.DateTimeField(blank=True, null=True)

    arentir = models.CharField(_("Street name (Arentir)"), max_length=255)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, related_name="events")

    event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name="events")

    def save(self, *args, **kwargs):
        if self.latitude is None and self.longitude is None:
            self.latitude, self.longitude = self.location.split(",")

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Position")
        verbose_name_plural = _("Position")
