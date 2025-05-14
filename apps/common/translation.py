from modeltranslation.translator import TranslationOptions, register

from apps.common import models


@register(models.About)
class AboutTranslationOption(TranslationOptions):
    fields = (
        "title",
        "content",
    )


@register(models.Region)
class RegionTranslationOption(TranslationOptions):
    fields = ("title",)


@register(models.Tag)
class TagTranslationOption(TranslationOptions):
    fields = ("title",)


@register(models.Post)
class PostTranslationOption(TranslationOptions):
    fields = (
        "title",
        "short_description",
        "content",
    )


@register(models.Event)
class EventTranslationOption(TranslationOptions):
    fields = (
        "title",
        "is_active",
    )


@register(models.Position)
class PositionTranslationOption(TranslationOptions):
    fields = (
        "title",
        "description",
        "arentir",
    )
