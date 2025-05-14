from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from django.conf.urls.i18n import set_language
from django.conf.urls.i18n import i18n_patterns
from django.views.generic.base import TemplateView  # new

from django.contrib.auth.forms import AuthenticationForm
from apps.common.api_endpoints.views import api as common


def configure_admin_login():
    if settings.DEBUG:
        return

    # captcha
    from django_recaptcha import fields

    class LoginForm(AuthenticationForm):
        captcha = fields.ReCaptchaField()

        def clean(self):
            captcha = self.cleaned_data.get("captcha")
            if not captcha:
                return
            return super().clean()

    admin.site.login_form = LoginForm
    admin.site.login_template = "login.html"


configure_admin_login()


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path("admin/", admin.site.urls),
    path("set_language/", set_language, name="set_language"),
    path("sentry-debug/", trigger_error),
    path("accounts/", include("allauth.urls")),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path("api/v1/", common.urls),
]

urlpatterns += i18n_patterns(path("", include("apps.common.urls")))
urlpatterns += i18n_patterns(path("", include("apps.book.urls")))

if settings.DEBUG:
    urlpatterns += [path("__reload__/", include("django_browser_reload.urls"))]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
