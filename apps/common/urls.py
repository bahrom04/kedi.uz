from django.urls import path, include
from apps.common import views


app_name = "common"

urlpatterns = [

    path("", views.HomeView.as_view(), name="home"),
    # path("contact", views.contact, name="contact"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("post/<int:id>", views.PostDetail.as_view(), name="post"),
    path("event/", views.EventListView.as_view(), name="event"),
    path("location/<int:id>", views.LocationsView.as_view(), name="location"),
    path(
        "location/detail/<int:id>",
        views.LocationDetailView.as_view(),
        name="location-detail",
    ),
    path('save_position/<int:position_id>/', views.save_position, name='save_position'),
    path('unsave_position/<int:position_id>/', views.unsave_position, name='unsave_position'),
    path("saved/", views.UserSavedView.as_view(), name="user_saved")
]
