from modeltranslation.translator import TranslationOptions, register

from apps.book import models


@register(models.Community)
class CommunityTranslationOption(TranslationOptions):
    fields = ("title","description",)

@register(models.AnimalType)
class AnimalTypeTranslationOption(TranslationOptions):
    fields = ("title",)
    
@register(models.GenderType)
class GenderTypeTranslationOption(TranslationOptions):
    fields = ("title",)
    
