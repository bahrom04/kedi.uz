from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from .schema import swagger_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("api/v1/common/", include("apps.common.urls", namespace="common")),
    path("api/v1/users/", include("apps.users.urls", namespace="users")),
    path(
        "ckeditor/upload/",
        serve,
        {"document_root": settings.MEDIA_ROOT, "show_indexes": True},
    ),
]

if settings.SWAGGER_ENABLED:
    urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
