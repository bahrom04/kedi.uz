from django.urls import include, path
from users import views


app_name = "users"

urlpatterns = [
    path("auth/", include("apps.users.auth.urls")),
]
