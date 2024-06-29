from django.views import generic
from apps.book import models


class CommunityListView(generic.ListView):
    template_name = "redesign/community.html"

    def get_queryset(self):
        queryset = models.Community.objects.all()
        return queryset
