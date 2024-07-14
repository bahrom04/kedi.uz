import sentry_sdk

from core.settings.base import *

DEBUG = False

ALLOWED_HOSTS = [
    "kedi.uz",
]

CSRF_TRUSTED_ORIGINS = [
    "https://kedi.uz",
]
CSRF_COOKIE_SECURE = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("DB_NAME"),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.str("DB_PASS"),
        "HOST": env.str("DB_HOST"),
        "PORT": env.str("DB_PORT"),
    }
}

TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = env.str("TELEGRAM_CHAT_ID")

SENTRY_KEY = env.str("SENTRY_KEY")

sentry_sdk.init(
    dsn=f"https://{SENTRY_KEY}.ingest.us.sentry.io/4507560080900096",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)
