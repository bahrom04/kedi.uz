from django.contrib import admin
from django.conf import settings
from apps.users import models
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _


# admin.site.site_header = _("Administration")
# admin.site.site_title = _("Management")


# class CustomGroupAdmin(admin.ModelAdmin):
#     readonly_fields = [
#         "name",
#     ]


# admin.site.unregister(Group)
# admin.site.register(Group, CustomGroupAdmin)


# Register your models here.
@admin.register(models.User)
class UserAdmin(DjangoUserAdmin):
    ordering = ("email",)
    list_display = ("id", "email", "first_name", "last_name")
    search_fields = ("first_name", "last_name", "email")
    list_display_links = ("id", "email")
    #     readonly_fields = ("last_login", "date_joined")
    list_per_page = 20

    def get_list_filter(self, request):
        list_filter = super().get_list_filter(request)
        if request.user.is_superuser:
            return list_filter

    def get_queryset(self, request):

        if request.user.is_superuser:
            return super().get_queryset(request)
        else:
            return super().get_queryset(request).filter(id=request.user.id)

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        # Check if the user belongs to the 'university manage' group

        if obj is not None and obj.is_superuser:
            # Modify fieldsets to remove the 'Permissions' tab
            fieldsets = (
                (None, {"fields": ("email", "password")}),
                (_("Personal info"), {"fields": ("first_name", "last_name", "photo")}),
                (
                    _("Permissions"),
                    {
                        "fields": (
                            "is_active",
                            "is_staff",
                            "is_superuser",
                            "position",
                            "groups",
                            "user_permissions",
                        ),
                    },
                ),
                (_("Important dates"), {"fields": ("last_login", "date_joined")}),
            )
        return fieldsets


