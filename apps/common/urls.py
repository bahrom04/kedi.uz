from django.urls import path, include
from apps.common import views


app_name = "common"

urlpatterns = [

    
    path("", views.HomeView.as_view(), name="home"),
    # path("contact", views.contact, name="contact"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("post/<slug:slug>", views.PostDetail.as_view(), name="post"),
    path("event/", views.EventListView.as_view(), name="event"),
    path("location/<int:id>", views.LocationsView.as_view(), name="location"),
    path(
        "location/detail/<int:id>",
        views.LocationDetailView.as_view(),
        name="location-detail",
    ),
]
