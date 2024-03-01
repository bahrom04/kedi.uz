from django.urls import path, include
from apps.common.views import index


app_name = "common"

urlpatterns = [path("", index)]
