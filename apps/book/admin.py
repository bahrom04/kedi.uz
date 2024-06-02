from django.contrib import admin
from core.mixins import TabbedTranslationAdmin
from apps.book import models

@admin.register(models.Community)
class CommunityAdmin(TabbedTranslationAdmin):
    pass