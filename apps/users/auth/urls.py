from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from users.auth import views

urlpatterns = [
    path("registration/", views.RegistrationView.as_view(), name="registration"),
    path("registration/verify/", views.RegistrationVerifyView.as_view(), name="registration_verify"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("login/refresh/", jwt_views.TokenRefreshView.as_view(), name="login_refresh"),
    path("password/reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path("check-account/", views.CheckAccountView.as_view(), name="check_account"),
]
