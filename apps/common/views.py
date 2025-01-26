from typing import Any
from django.http import HttpRequest, JsonResponse, HttpResponseForbidden
from django.core.cache import cache
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.common.models import Event, About, Post, Position, UserSavedPosition


class HomeView(generic.ListView):
    template_name = "redesign/home.html"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any):
        home_posts_cache_key = f"home_posts_cache_key"
        posts = cache.get(home_posts_cache_key)

        if not posts:
            posts = list(Post.objects.order_by("-created_at").prefetch_related("tag"))
            cache.set(home_posts_cache_key, posts, 60 * 5)

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

        event_cache_key = f"positions_event_{event_id}"
        posotions = cache.get(event_cache_key)

        if not posotions:
            posotions = list(
                Position.objects.filter(event_id=event_id)
                .values(
                    "id", "latitude", "longitude", "title", "thumbnail"
                )[:100]
            )
            cache.set(event_cache_key, posotions, 60 * 5)

        user_saved_positions = []

        if request.user.is_authenticated:
            user_saved_positions = list(
                UserSavedPosition.objects.filter(user=request.user)
                .select_related("user", "position")
                .values_list(
                    "position_id", flat=True
                )
            )

        event_title = Event.objects.get(pk=event_id)

        return render(
            request,
            "redesign/location.html",
            context={
                "positions": posotions,
                "user_saved_positions": user_saved_positions,
                "event_title": event_title,
            },
        )


class LocationDetailView(generic.DetailView):
    model = Position
    template_name = "redesign/location_detail.html"
    context_object_name = "position_detail"

    def get_object(self):
        position_id = self.kwargs["id"]
        posotion_detail = Position.objects.get(id=position_id)
        return posotion_detail


def save_position(request, position_id):
    if not request.user.is_authenticated:
        return HttpResponseForbidden({"status": "fuck you"})
    else:
        position = Position.objects.get(id=position_id)
        saved_position, created = UserSavedPosition.objects.get_or_create(
            user=request.user, position=position
        )
        if created:
            return JsonResponse({"status": "saved"})
    return JsonResponse({"status": "already_saved"})


def unsave_position(request, position_id):
    if not request.user.is_authenticated:
        return HttpResponseForbidden({"status": "fuck you"})
    try:
        saved_position = UserSavedPosition.objects.get(
            user=request.user, position_id=position_id
        )
        saved_position.delete()
        return JsonResponse({"status": "unsaved"})
    except UserSavedPosition.DoesNotExist:
        return JsonResponse({"status": "not_saved"})


class UserSavedView(LoginRequiredMixin, generic.ListView):
    model = UserSavedPosition
    context_object_name = "user_saved"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any):
        user_saved = list(UserSavedPosition.objects.filter(
            user=self.request.user
        ).select_related("user", "position"))
        
        return render(
            request,
            template_name="redesign/user_saved.html",
            context={"user_saved": user_saved},
        )
