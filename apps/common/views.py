from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.http import HttpResponse
from apps.common.models import Position
from apps.common.models import Post


# def index(request):
#     posotions = list(
#         Position.objects.filter(event__title="Hashar").values("latitude", "longitude")
#     )
#     print(posotions)
#     context = {}
#     return render(request, "index.html", context={"positions": posotions})


class HomeView(generic.ListView):
    model = Post
    template_name = "index.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.all()


class AboutView(generic.ListView):
    model = Post
    template_name = "about.html"


class PostList(generic.ListView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        slug = self.kwargs["slug"]
        return Post.objects.get(slug=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        slug = self.kwargs["slug"]
        post = get_object_or_404(Post, slug=slug)

        context["post"] = post

        tags = post.tag.all()
        context["tags"] = tags

        if post:
            post.views += 1
            post.save()

        return context
