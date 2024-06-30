from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from django.conf.urls.i18n import set_language
from django.conf.urls.i18n import i18n_patterns
from django.views.generic.base import TemplateView  # new

# captcha
from django.contrib.auth.forms import AuthenticationForm
from captcha import fields

from apps.common.api_endpoints.views import api as common

# class LoginForm(AuthenticationForm):
#     captcha = fields.ReCaptchaField()

#     def clean(self):
#         captcha = self.cleaned_data.get("captcha")
#         if not captcha:
#             return
#         return super().clean()


# admin.site.login_form = LoginForm
# admin.site.login_template = "login.html"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("set_language/", set_language, name="set_language"),
    path(
        "ckeditor/upload/",
        serve,
        {"document_root": settings.MEDIA_ROOT, "show_indexes": True},
    ),
    path("accounts/", include("allauth.urls")),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path("api/", common.urls),
]

urlpatterns += i18n_patterns(path("", include("apps.common.urls")))
urlpatterns += i18n_patterns(path("", include("apps.book.urls")))

if settings.DEBUG:
    urlpatterns += [path("__reload__/", include("django_browser_reload.urls"))]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
