import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinValueValidator, MaxValueValidator


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.id


class Media(BaseModel):
    class MediaType(models.TextChoices):
        VIDEO = "video", _("Video")
        IMAGE = "image", _("Image")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(_("File"), upload_to="uploads/%Y/%m/%d/")
    file_type = models.CharField(_("File Type"), choices=MediaType.choices, max_length=255)

    class Meta:
        verbose_name = _("Media")
        verbose_name_plural = _("Media")


# class Country(TimeStampedModel):
#     name = models.CharField(_('Country'), max_length=255)
#     icon = models.ForeignKey(Media, on_delete=models.PROTECT, related_name='countries', verbose_name=_('Icon'))

#     class Meta:
#         db_table = 'Country'
#         verbose_name = _('Country')
#         verbose_name_plural = _('Countries')
#         ordering = ('name',)

#     def __str__(self):
#         return self.name


class Region(BaseModel):
    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="regions",
        verbose_name=_("Parent"),
    )
    title = models.CharField(_("Title"), max_length=255)

    class Meta:
        db_table = "Region"
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")
        ordering = ("title",)


class Blog(BaseModel):
    title = models.CharField(_("Title"), max_length=255)
    background_image = models.ForeignKey(
        Media,
        on_delete=models.PROTECT,
        related_name="blogs",
        verbose_name=_("Background image"),
    )
    description = RichTextUploadingField(_("Description"))

    class Meta:
        db_table = "Blog"
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")
        ordering = ("title",)


class Event(BaseModel):
    title = models.CharField(_("Title"), max_length=255)

    is_active = models.BooleanField(_("Is active"), default=True)
    type = models.CharField(_("Type"), max_length=255)
    region = models.ForeignKey(
        "common.Region", on_delete=models.PROTECT, related_name="events"
    )

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
        ordering = ("-created_at",)
