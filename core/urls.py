from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from .schema import swagger_urlpatterns


urlpatterns = [
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("admin/", admin.site.urls),
    path(
        "ckeditor/upload/",
        serve,
        {"document_root": settings.MEDIA_ROOT, "show_indexes": True},
    ),
    path("", include("apps.common.urls")),
    path("accounts/", include("apps.users.urls", namespace="users")),
    path("accounts/", include("django.contrib.auth.urls")),
    # path("", TemplateView.as_view(template_name="home.html"), name="home")
]

if settings.SWAGGER_ENABLED:
    urlpatterns += swagger_urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
