from django.urls import path, include
from apps.common import views


# app_name = "common"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("index/", views.HomeView.as_view(), name="home"),
    # path("contact", views.contact, name="contact"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("post/<slug:slug>", views.PostList.as_view(), name="post"),
]
