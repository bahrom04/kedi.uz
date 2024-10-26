from django.contrib import admin
from core.mixins import TabbedTranslationAdmin
from apps.book import models

@admin.register(models.Community)
class CommunityAdmin(TabbedTranslationAdmin):
    pass

@admin.register(models.AnimalType)
class AnimalTypeAdmin(TabbedTranslationAdmin):
    pass
@admin.register(models.GenderType)
class GenderTypeAdmin(TabbedTranslationAdmin):
    pass

@admin.register(models.LostAnimal)
class LostPetAdmin(TabbedTranslationAdmin):
    pass