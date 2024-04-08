import json
from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.core.serializers.json import DjangoJSONEncoder
from apps.common.models import Position, Event
from apps.common.models import Post


class HomeView(generic.ListView):
    model = Post
    template_name = "index.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.all()

    def post(self, request, *args, **kwargs):
        if 'language' in request.POST:
            language = request.POST.get('language', 'en')
            request.session['django_language'] = language
        return self.get(request, *args, **kwargs)


class AboutView(generic.ListView):
    model = Post
    template_name = "about.html"


class PostDetail(generic.DeleteView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"

    def get_object(self):
        post_id = self.kwargs["id"]
        return Post.objects.get(id=post_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post_id = self.kwargs["id"]
        post = get_object_or_404(Post, id=post_id)

        context["post"] = post

        tags = post.tag.all()
        context["tags"] = tags

        if post:
            post.views += 1
            post.save()

        return context


class EventListView(generic.ListView):
    model = Event
    template_name = "event.html"

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset


class LocationsView(generic.ListView):
    model = Position
    template_name = "location.html"
    context_object_name = "positions"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any):
        event_id = self.kwargs["id"]
        posotions = list(
            Position.objects.filter(event_id=event_id).values(
                "id", "latitude", "longitude", "title", "description"
            )[:100]
        )
        event_title = Event.objects.get(pk=event_id)
        return render(
            request,
            "location.html",
            context={"positions": posotions, "event_title": event_title},
        )


class LocationDetailView(generic.DetailView):
    model = Position
    template_name = "location_detail.html"
    context_object_name = "position_detail"

    def get_object(self):
        position_id = self.kwargs["id"]
        posotion_detail = Position.objects.get(id=position_id)
        return posotion_detail
