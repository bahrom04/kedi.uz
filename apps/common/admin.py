from django.contrib import admin
from core.mixins import TabbedTranslationAdmin
from apps.common import models


@admin.register(models.Media)
class MediaAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.About)
class AboutAdmin(TabbedTranslationAdmin):
    list_display = (
        "title",
        "created_at",
        "updated_at",
    )


@admin.register(models.Region)
class RegionAdmin(TabbedTranslationAdmin):
    list_display = ("title",)


@admin.register(models.Post)
class PostAdmin(TabbedTranslationAdmin):
    list_display = (
        "title",
        "created_at",
        "views",
    )


@admin.register(models.Tag)
class TagAdmin(TabbedTranslationAdmin):
    pass


@admin.register(models.Event)
class EventAdmin(TabbedTranslationAdmin):
    list_display = (
        "title",
        "created_at",
        "updated_at",
        "is_active",
    )


@admin.register(models.Position)
class PositionAdmin(TabbedTranslationAdmin):
    list_display = (
        "title",
        "region",
        "event",
        "created_at",
        "updated_at",
    )
    list_select_related = (
        "region",
        "event",
    )
    exclude = ("latitude", "longitude")


@admin.register(models.UserSavedPosition)
class UserSavedPositionAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "position",
    )
    list_select_related = (
        "user",
        "position",
    )
