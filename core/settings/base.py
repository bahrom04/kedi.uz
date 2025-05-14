from pathlib import Path
from dotenv import load_dotenv
import os
from django.utils.translation import gettext_lazy as _


load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.getenv("DEBUG")

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",")


# Application definition
DJANGO_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
]

CUSTOM_APPS = [
    "apps.common.apps.CommonConfig",
    "apps.users.apps.UsersConfig",
    "apps.book.apps.BookConfig",
    "theme",
]

THIRD_PARTY_APPS = [
    "modeltranslation",
    "tailwind",
    "django_browser_reload",
    "location_field.apps.DefaultConfig",
]

INSTALLED_APPS = DJANGO_APPS + CUSTOM_APPS + THIRD_PARTY_APPS


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


SITE_ID = 4

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": ["profile", "email"],
        "AUTH_PARAMS": {"access_type": "online"},
        "APP": {
            "client_id": os.getenv("CLIENT_ID"),
            "secret": os.getenv("SECRET"),
            "key": "",  # Leave key blank for Google
        },
    },
    # Add configurations for other social providers as needed
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # customs
    "core.middleware.BlockInvalidHostsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
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

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
]


WSGI_APPLICATION = "core.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


LANGUAGE_CODE = "en"
LANGUAGES = (
    ("en", _("English")),
    ("uz", _("Uzbek")),
    ("ru", _("Russian")),
)

TIME_ZONE = "Asia/Tashkent"
DATE_INPUT_FORMATS = [
    '%Y-%m-%d',  # Django default format
    '%d.%m.%Y',  # Russian/Uzbek format
    '%m/%d/%Y',  # English format
]

USE_I18N = True
USE_L10N = True
USE_TZ = True


MODELTRANSLATION_DEFAULT_LANGUAGE = "uz"

gettext = lambda s: s

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

MODELTRANSLATION_PREPOPULATE_LANGUAGE = "en"

LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)


# auth
AUTH_USER_MODEL = "users.User"


# STATIC
STATIC_URL = "static/"
STATICFILES_DIRS = (BASE_DIR / "staticfiles",)
STATIC_ROOT = BASE_DIR / "static"


MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOCATION_FIELD = {
    "map.provider": "openstreetmap",
    "search.provider": "nominatim",
}

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# TailwindCss
TAILWIND_APP_NAME = "theme"
INTERNAL_IPS = [
    "127.0.0.1",
]
NPM_BIN_PATH = os.getenv("NPM_BIN_PATH")

# Security settings
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = False # Redirect all HTTP requests to HTTPS
SESSION_COOKIE_SECURE = False  # Use secure cookies
CSRF_COOKIE_SECURE = False # Use secure CSRF cookies


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/0', 
    }
}

