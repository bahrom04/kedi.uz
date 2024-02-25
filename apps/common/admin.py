from django.contrib import admin
from apps.common import models


# Register your models here.
@admin.register(models.Media)
class MediaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Position)
class PositionAdmin(admin.ModelAdmin):
    exclude = ('latitude', 'longitude')



