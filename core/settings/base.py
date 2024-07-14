import environ

from pathlib import Path
from django.utils.translation import gettext_lazy as _

env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = env.str("DJANGO_SECRET_KEY")

DJANGO_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

CUSTOM_APPS = [
    "apps.book",
    "apps.users",
    "apps.theme",
    "apps.common",
]

THIRD_PARTY_APPS = [
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "tailwind",
    "django_browser_reload",
    "ckeditor",
    "ckeditor_uploader",
    "location_field",
    "modeltranslation",
    "captcha",
]

INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    # django middlewares
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # third party middlewares
    "allauth.account.middleware.AccountMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    # custom middlewares
    "core.middleware.ErrorHandlerMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR, "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "core.context_processors.top_communities",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

TIME_ZONE = "Asia/Tashkent"

USE_L10N = True
USE_I18N = True
USE_TZ = True

LANGUAGE_CODE = "en"
LANGUAGES = (
    ("en", _("English")),
    ("ru", _("Russian")),
    ("uz", _("Uzbek")),
)
LOCALE_PATHS = (BASE_DIR / "locales/",)

MODELTRANSLATION_LANGUAGES = (
    "uz",
    "ru",
    "en",
)
MODELTRANSLATION_FALLBACK_LANGUAGES = {
    "default": (
        "uz",
        "ru",
        "en",
    ),
    "uz": (
        "ru",
        "en",
    ),
    "en": (
        "uz",
        "ru",
    ),
    "ru": (
        "uz",
        "en",
    ),
}
MODELTRANSLATION_DEFAULT_LANGUAGE = "uz"
MODELTRANSLATION_PREPOPULATE_LANGUAGE = "en"

STATICFILES_DIRS = (BASE_DIR / "staticfiles",)

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

CKEDITOR_CONFIGS = {
    "default": {
        "config.versionCheck": False,
        "toolbar": "full",
        "height": 300,
        "width": 700,
    }
}
CKEDITOR_JQUERY_URL = "//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"
CKEDITOR_THUMBNAIL_SIZE = (450, 300)
CKEDITOR_IMAGE_BACKEND = "pillow"

LOCATION_FIELD = {
    "map.provider": "openstreetmap",
    "search.provider": "nominatim",
}

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

TAILWIND_APP_NAME = "apps.theme"
NPM_BIN_PATH = env.str("TAILWIND_NPM_PATH")
INTERNAL_IPS = ("127.0.0.1",)

RECAPTCHA_PUBLIC_KEY = env.str("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = env.str("RECAPTCHA_PRIVATE_KEY")

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

SITE_ID = 4

AUTH_USER_MODEL = "users.User"

AUTHENTICATION_BACKENDS = [
    "allauth.account.auth_backends.AuthenticationBackend",
]

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": ["profile", "email"],
        "AUTH_PARAMS": {"access_type": "online"},
        "APP": {
            "client_id": env.str("GOOGLE_CLIEND_ID"),
            "secret": env.str("GOOGLE_SECRET"),
            "key": "",
        },
    },
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

CKEDITOR_UPLOAD_PATH = "uploads/"

# import sentry_sdk

# sentry_key = env.str("SENTRY_KEY")

# sentry_sdk.init(
#     dsn=f"https://{sentry_key}.ingest.us.sentry.io/4507560080900096",
#     traces_sample_rate=1.0,
#     profiles_sample_rate=1.0,
# )
