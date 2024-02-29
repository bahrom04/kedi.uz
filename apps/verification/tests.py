from django.core import mail
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase

from verification.models import VerificationSession
from verification.templates import VERIFICATION_EMAIL_TEMPLATES


class TestRequestOTP(APITestCase):
    api = reverse("verification:request-otp")

    def test_email_reset_password_happy(self):
        data = {
            "type": VerificationSession.Types.EMAIL,
            "address": "test@mail.com",
            "purpose": VerificationSession.Purposes.RESET_PASSWORD,
            "client_secret": "testSecret",
        }
        response = self.client.post(self.api, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(VerificationSession.objects.count(), 1)
        session = VerificationSession.objects.get()
        self.assertEqual(response.json()["sid"], session.id)
        self.assertEqual(response.json()["wait"], 60)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, [session.address])
        subject = session.get_purpose_display()
        self.assertEqual(mail.outbox[0].subject, subject)
        body = VERIFICATION_EMAIL_TEMPLATES[session.purpose].format(otp=session.otp)
        self.assertEqual(mail.outbox[0].body, body)

    def test_email_reset_password_with_invalid_email(self):
        data = {
            "type": VerificationSession.Types.EMAIL,
            "address": "testmail.com",
            "purpose": VerificationSession.Purposes.RESET_PASSWORD,
            "client_secret": "testSecret",
        }
        response = self.client.post(self.api, data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["address"][0].code, "invalid_email_address")

    def test_email_reset_password_same_sid_for_subsequent_client_secret(self):
        data = {
            "type": VerificationSession.Types.EMAIL,
            "address": "test@mail.com",
            "purpose": VerificationSession.Purposes.RESET_PASSWORD,
            "client_secret": "testSecret",
        }
        response = self.client.post(self.api, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(VerificationSession.objects.count(), 1)
        session = VerificationSession.objects.get()
        self.assertEqual(response.data["sid"], session.id)

        response2 = self.client.post(self.api, data)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(VerificationSession.objects.count(), 1)
        self.assertEqual(response2.json()["sid"], session.id)

    def test_email_reset_password_different_sid_for_different_client_secret(self):
        data1 = {
            "type": VerificationSession.Types.EMAIL,
            "address": "test@mail.com",
            "purpose": VerificationSession.Purposes.RESET_PASSWORD,
            "client_secret": "test1",
        }
        response1 = self.client.post(self.api, data1)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(VerificationSession.objects.count(), 1)
        session1 = VerificationSession.objects.get()
        self.assertEqual(response1.data["sid"], session1.id)

        data2 = {
            "type": VerificationSession.Types.EMAIL,
            "address": "test@mail.com",
            "purpose": VerificationSession.Purposes.RESET_PASSWORD,
            "client_secret": "test2",
        }
        response2 = self.client.post(self.api, data2)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(VerificationSession.objects.count(), 2)

        session2 = VerificationSession.objects.get(client_secret="test2")
        self.assertEqual(response2.data["sid"], session2.id)


class TestSubmitOTP(APITestCase):
    api = reverse("verification:submit-otp")

    def test_happy(self):
        session = VerificationSession.objects.create(
            type=VerificationSession.Types.EMAIL,
            address="test@mail.com",
            client_secret="test",
            otp="123456",
            purpose=VerificationSession.Purposes.RESET_PASSWORD,
        )
        data = {
            "sid": session.id,
            "otp": "123456",
            "client_secret": "test",
        }
        response = self.client.post(self.api, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["sid"], session.id)
        self.assertEqual(response.json()["validated"], True)

    def test_with_invalid_sid(self):
        data = {
            "sid": 1,
            "otp": "123456",
            "client_secret": "test",
        }
        response = self.client.post(self.api, data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.data["non_field_errors"][0].code, "session_not_found")

    def test_with_invalid_client_secret(self):
        session = VerificationSession.objects.create(
            type=VerificationSession.Types.EMAIL,
            address="test@mail.com",
            client_secret="test",
            otp="123456",
            purpose=VerificationSession.Purposes.RESET_PASSWORD,
        )
        data = {
            "sid": session.id,
            "otp": "123456",
            "client_secret": "test2",
        }
        response = self.client.post(self.api, data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["non_field_errors"][0].code, "session_not_found")

    def test_with_invalid_otp(self):
        session = VerificationSession.objects.create(
            type=VerificationSession.Types.EMAIL,
            address="test@mail.com",
            client_secret="test",
            otp="123456",
            purpose=VerificationSession.Purposes.RESET_PASSWORD,
        )
        data = {
            "sid": session.id,
            "otp": "123457",
            "client_secret": "test",
        }
        response = self.client.post(self.api, data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["otp"][0].code, "invalid_otp")

    def test_too_many_invalid_attempts(self):
        session = VerificationSession.objects.create(
            type=VerificationSession.Types.EMAIL,
            address="test@mail.com",
            client_secret="test",
            otp="123456",
            purpose=VerificationSession.Purposes.RESET_PASSWORD,
        )

        data = {
            "sid": session.id,
            "otp": "111222",
            "client_secret": "test",
        }

        for i in range(1, 3):
            with self.subTest(attempt=i):
                response = self.client.post(self.api, data)
                self.assertEqual(response.status_code, 400)
                self.assertEqual(len(response.data), 1)
                self.assertEqual(response.data["otp"][0].code, "invalid_otp")

        with self.subTest(attempt=3):
            response = self.client.post(self.api, data)
            self.assertEqual(response.status_code, 400)
            self.assertEqual(len(response.data), 1)
            self.assertEqual(response.data["non_field_errors"][0].code, "too_many_invalid_attempts")

    def test_with_expired_session(self):
        session = VerificationSession.objects.create(
            type=VerificationSession.Types.EMAIL,
            address="test@mail.com",
            client_secret="test",
            otp="123456",
            purpose=VerificationSession.Purposes.RESET_PASSWORD,
        )
        session.created_at = timezone.now() - timezone.timedelta(minutes=10)
        session.save()

        data = {
            "sid": session.id,
            "otp": "123456",
            "client_secret": "test",
        }
        response = self.client.post(self.api, data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["non_field_errors"][0].code, "session_not_found")
