from django.urls import include, path
from apps.users import views


app_name = "users"

urlpatterns = [
    path("", include("apps.users.auth.urls")),
]
