from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("i18n/", include("django.conf.urls.i18n")),
    path(
        "ckeditor/upload/",
        serve,
        {"document_root": settings.MEDIA_ROOT, "show_indexes": True},
    ),
    path("", include("apps.common.urls")),
    path("accounts/", include("apps.users.urls", namespace="users")),
    path("accounts/", include("django.contrib.auth.urls")),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
