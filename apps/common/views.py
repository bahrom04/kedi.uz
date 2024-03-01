from django.shortcuts import render
from django.http import HttpResponse
from apps.common.models import Position


def index(request):
    posotions = list(Position.objects.values("latitude", "longitude")[:100])
    print(posotions)
    context = {}
    return render(request, "index.html", context={"positions": posotions})
