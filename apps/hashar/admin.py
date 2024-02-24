from django.contrib import admin
from apps.hashar import models

@admin.register(models.HasharDetail)
class HasharDetailAdmin(admin.ModelAdmin):
    pass