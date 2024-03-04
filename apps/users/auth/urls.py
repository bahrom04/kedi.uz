from django.urls import path
from apps.users.auth import views

urlpatterns = [
    path("register/", views.UserRegisterView.as_view(), name="registration"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path("detail/", views.UserDetailView.as_view(), name="detail"),
]
