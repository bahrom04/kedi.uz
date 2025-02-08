from .base import *  # noqa

DEBUG = False

CSRF_TRUSTED_ORIGINS = [
    "https://kedi.uz"
]

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


import sentry_sdk

sentry_key = os.getenv("sentry_key")

sentry_sdk.init(
    dsn=f"https://{sentry_key}.ingest.us.sentry.io/4507560080900096",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)
