from modeltranslation.translator import TranslationOptions, register

from apps.book import models


@register(models.Community)
class CommunityTranslationOption(TranslationOptions):
    fields = ("title",)
