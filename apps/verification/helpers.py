from __future__ import annotations

from typing import Literal

from django.utils import timezone

from verification.models import VerificationSession
from verification.utils import generate_otp


class SessionNotFoundError(Exception):
    pass


class InvalidOTPError(Exception):
    def __init__(self, session):
        self.session = session


class TooManyInvalidOTPError(Exception):
    pass


class VerificationHelper:
    SessionNotFoundError = SessionNotFoundError
    InvalidOTPError = InvalidOTPError
    TooManyInvalidOTPError = TooManyInvalidOTPError

    @staticmethod
    def get_or_create_session(type_: Literal["phone", "email"], purpose, address, client_secret) -> VerificationSession:
        if session := VerificationSession.objects.filter(
            type=type_,
            address=address,
            client_secret=client_secret,
            purpose=purpose,
            validated=False,
            expired=False,
            created_at__gte=timezone.now() - timezone.timedelta(minutes=5),
        ).first():
            return session

        return VerificationSession.objects.create(
            type=type_, address=address, client_secret=client_secret, otp=generate_otp(), purpose=purpose
        )

    @staticmethod
    def validate_session(sid, client_secret, otp) -> VerificationSession:
        session = VerificationSession.objects.filter(
            id=sid, client_secret=client_secret, created_at__gt=timezone.now() - timezone.timedelta(minutes=10)
        ).first()
        if not session:
            raise SessionNotFoundError()

        if session.invalid_attempts >= 3:
            raise TooManyInvalidOTPError()

        if session.expired:
            raise SessionNotFoundError()

        if session.otp != otp:
            session.invalid_attempts += 1
            session.save()
            if session.invalid_attempts >= 3:
                session.expired = True
                session.save()
                raise TooManyInvalidOTPError()
            raise InvalidOTPError(session)

        if not session.validated:
            session.validated = True
            session.validated_at = timezone.now()
            session.save(update_fields=["validated", "validated_at"])

        return session

    @staticmethod
    def get_validated_session(sid, client_secret) -> VerificationSession:
        session = VerificationSession.objects.filter(
            id=sid,
            client_secret=client_secret,
            validated=True,
            expired=False,
            validated_at__gt=timezone.now() - timezone.timedelta(minutes=10),
        ).first()

        if not session:
            raise SessionNotFoundError()

        return session
