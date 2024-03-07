from django.urls import include, path


app_name = "users"

urlpatterns = [
    path("", include("apps.users.auth.urls")),
]
