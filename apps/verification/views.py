from django.conf import settings

from common.generics import MutateView
from verification import models, serializers


class RequestOTPView(MutateView):
    serializer_class = serializers.RequestOTPSerializer

    def perform_mutate(self, serializer):
        session: models.VerificationSession = serializer.save()
        if settings.EMAIL_WORKING:
            session.send_otp()


class SubmitOTPView(MutateView):
    serializer_class = serializers.SubmitOTPSerializer
