from django.views import generic
from apps.book import models
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LostAnimalForm

class CommunityListView(generic.ListView):
    template_name = "redesign/community.html"

    def get_queryset(self):
        return models.Community.objects.all()
    
class LostAnimalListView(generic.ListView):
    template_name = "redesign/lost_animal_list.html"

    def get(self, request: HttpRequest):
        posts = list(models.LostAnimal.objects.all())

        return render(
            request,
            "redesign/lost_animal_list.html",
            context={"posts": posts},
        )

@login_required
def post_lost_animal(request):
    if request.method == 'POST':
        print("POST data:", request.POST)
        print("Title:", request.POST.get('title'))
        print("Date Lost:", request.POST.get('date_lost'))

        form = LostAnimalForm(request.POST, request.FILES)
        if form.is_valid():
            lost_animal = form.save(commit=False)
            lost_animal.posted_by = request.user
            lost_animal.save()
            return redirect('/')  # Redirect after successful post
    else:
        form = LostAnimalForm()
    return render(request, 'redesign/lost_animal_form.html', {'form': form})
