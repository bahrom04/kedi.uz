from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from .schema import swagger_urlpatterns
from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "ckeditor/upload/",
        serve,
        {"document_root": settings.MEDIA_ROOT, "show_indexes": True},
    ),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("api/v1/common/", include("apps.common.urls", namespace="common")),
    path("accounts/", include("apps.users.urls", namespace="users")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home")
]

if settings.SWAGGER_ENABLED:
    urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
