from django.urls import path
from apps.book import views

app_name = "book"


urlpatterns = [
    path("community/", views.CommunityListView.as_view(), name="community"),
    path("lost-animal-list/", views.LostAnimalListView.as_view(), name="lost-animal-list"),
    path("lost-animal/", views.post_lost_animal, name="lost-animal"),
    path(
        "lost-animal/detail/<int:id>",
        views.LostAnimalDetail.as_view(),
        name="lost-animal-detail",
    ),
]