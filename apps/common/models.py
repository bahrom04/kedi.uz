from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from django.conf import settings

from location_field.models.plain import PlainLocationField


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


class About(BaseModel):
    image = models.ImageField(upload_to="images/", blank=True)
    title = models.CharField(_("Title"), max_length=128)
    content = models.TextField(_("Content"))

    class Meta:
        verbose_name = _("About")
        verbose_name_plural = _("About")


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

    title = models.CharField(
        _("Street name (Arentir)"),
        max_length=255,
        unique=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Region"
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")


class Tag(models.Model):
    title = models.CharField(_("Title"), max_length=128)

    def tag_name(self):
        return self.title

    def __str__(self):
        return self.title


class Post(models.Model):
    image = models.ImageField(upload_to="posts/", blank=True)
    title = models.CharField(
        _("Title"),
        max_length=256,
    )
    short_description = models.CharField(
        _("Short Description"),
        max_length=256,
    )
    content = models.TextField(_("Content"))
    tag = models.ManyToManyField(Tag, related_name="tag", blank=True)

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

    title = models.CharField(
        _("Event Type"),
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(_("Is active"), default=True)

    image = models.ImageField(upload_to="event/", blank=True)

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")


class Position(BaseModel):
    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"))
    thumbnail = models.ImageField(upload_to="position", null=True, blank=True)

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


class UserSavedPosition(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "position")

    def __str__(self):
        return f"{self.user}' saved position: {self.position.title}"
