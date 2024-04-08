from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify

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


class Tag(models.Model):
    title = models.CharField(max_length=128)

    def tag_name(self):
        return self.title

    def __str__(self):
        return self.title


class Post(models.Model):
    image = models.ImageField(upload_to="images/", blank=True)
    title = models.CharField(
        _("Title"),
        max_length=256,
    )
    short_description = models.CharField(
        _("Short Description"),
        max_length=256,
    )
    content = RichTextUploadingField(_("Content"))
    tag = models.ManyToManyField(Tag, related_name="posts", blank=True)

    views = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("post", kwargs={"id": self.id})


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
    title = models.CharField(_("Title"), max_length=255)
    description = RichTextUploadingField(_("Description"))

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

    def get_absolute_url(self):
        return reverse_lazy("location", kwargs={"id": self.id})

    class Meta:
        verbose_name = _("Position")
        verbose_name_plural = _("Position")
