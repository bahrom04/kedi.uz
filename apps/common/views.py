from typing import Any
from django.db.models.base import Model as Model
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render
from django.views import generic
from apps.common.models import Position, Event, About
from apps.common.models import Post

from allauth.socialaccount.models import SocialAccount


class HomeView(generic.ListView):
    template_name = "redesign/home.html"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any):
        posts = Post.objects.all()
        return render(
            request,
            "redesign/home.html",
            context={"posts": posts},
        )


class AboutView(generic.ListView):
    model = Post
    template_name = "redesign/about.html"
    context_object_name = "about"

    def get_queryset(self):
        queryset = About.objects.all()[0]
        return queryset


class PostDetail(generic.DetailView):
    model = Post
    template_name = "redesign/post_detail.html"
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
    template_name = "redesign/event.html"

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset


class LocationsView(generic.ListView):
    model = Position
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
            "redesign/location.html",
            context={"positions": posotions, "event_title": event_title},
        )


class LocationDetailView(generic.DetailView):
    model = Position
    template_name = "redesign/location_detail.html"
    context_object_name = "position_detail"

    def get_object(self):
        position_id = self.kwargs["id"]
        posotion_detail = Position.objects.get(id=position_id)
        return posotion_detail
