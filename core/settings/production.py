from .base import *  # noqa

DEBUG = False

INSTALLED_APPS += [
    "django_recaptcha"
]

CSRF_TRUSTED_ORIGINS = ["https://kedi.uz"]

# captcha
RECAPTCHA_PUBLIC_KEY = os.getenv("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = os.getenv("RECAPTCHA_PRIVATE_KEY")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


import sentry_sdk

SENTRY_KEY = os.getenv("SENTRY_KEY")

sentry_sdk.init(
    dsn=f"https://{SENTRY_KEY}.ingest.us.sentry.io/4507560080900096",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)
