from django.urls import path
from apps.book import views

app_name = "book"


urlpatterns = [
    path("community/", views.CommunityListView.as_view(), name="community")
]