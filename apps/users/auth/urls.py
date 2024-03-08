from django.urls import path
from apps.users.auth import views

urlpatterns = [
    path("register/", views.UserRegisterView.as_view(), name="registration"),
]
