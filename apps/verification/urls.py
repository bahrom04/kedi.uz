from django.urls import path

from verification import views

app_name = "verification"

urlpatterns = [
    path("request-otp/", views.RequestOTPView.as_view(), name="request-otp"),
    path("submit-otp/", views.SubmitOTPView.as_view(), name="submit-otp"),
]
