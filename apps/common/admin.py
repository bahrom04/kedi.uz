from django.contrib import admin
from core.mixins import TabbedTranslationAdmin
from apps.common import models


@admin.register(models.Media)
class MediaAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.About)
class AboutAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.Region)
class RegionAdmin(TabbedTranslationAdmin):
    list_display = ("type",)


@admin.register(models.Post)
class PostAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.Tag)
class TagAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.Event)
class EventAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.Position)
class PositionAdmin(TabbedTranslationAdmin):
    exclude = ("latitude", "longitude")
