from django.utils.crypto import get_random_string


def generate_otp():
    return get_random_string(length=6, allowed_chars="1234567890")
