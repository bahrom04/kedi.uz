from django.contrib import admin

from verification import models


@admin.register(models.VerificationSession)
class VerificationSessionAdmin(admin.ModelAdmin):
    list_display = [
        "type",
        "address",
        "expired",
        "validated",
        "purpose",
        "created_at",
        "validated_at",
    ]
    list_filter = ["expired", "validated", "purpose"]
    search_fields = ["address"]

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
