from django.views import generic
from apps.book import models
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .forms import LostAnimalForm

from django.core import serializers
from . import models

from pydantic import BaseModel
from django.core.serializers import serialize
import json

class CommunityModel(BaseModel):
    pk: int
    title: str
    image: str
    description: str = ""
    telegram_link: str

    @classmethod
    def from_django(cls, instance):
        instance_data = json.loads(serialize('json', [instance]))[0]['fields']
        description = instance_data.get('description') or ""
        instance_data['description'] = description.replace('\r', '').replace('\n', '<br>')
        return cls(pk=instance.pk, **instance_data)
    

class CommunityListView(generic.ListView):
    template_name = "redesign/community.html"
    
    def get(self, request, *args, **kwargs):
        communities = models.Community.objects.all()
        formatted_communities = [CommunityModel.from_django(community).dict() for community in communities]
        # print(formatted_communities)
        return render(request, 'redesign/community.html', {'json_data': json.dumps(formatted_communities)})
    

class LostAnimalListView(generic.ListView):
    template_name = "redesign/lost_animal_list.html"

    def get(self, request: HttpRequest):
        posts = list(models.LostAnimal.objects.order_by("-created_at"))

        return render(
            request,
            "redesign/lost_animal_list.html",
            context={"posts": posts},
        )

class LostAnimalDetail(generic.DetailView):
    model = models.LostAnimal
    template_name = "redesign/lost_animal_detail.html"
    context_object_name = "post"

    def get_object(self):
        post_id = self.kwargs["id"]
        return models.LostAnimal.objects.get(id=post_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post_id = self.kwargs["id"]
        post = get_object_or_404(models.LostAnimal, id=post_id)

        context["post"] = post

        return context

@login_required
def post_lost_animal(request):
    if request.method == 'POST':
        form = LostAnimalForm(request.POST, request.FILES)
        if form.is_valid():
            lost_animal = form.save(commit=False)
            lost_animal.posted_by = request.user
            lost_animal.save()
            return redirect('/lost-animal-list/')
    else:
        form = LostAnimalForm()
    return render(request, 'redesign/lost_animal_form.html', {'form': form})
