from django.shortcuts import render
from django.http import HttpResponse
from apps.common.models import Position


def index(request):
    posotions = list(
        Position.objects.filter(event__title="Hashar").values("latitude", "longitude")
    )
    print(posotions)
    context = {}
    return render(request, "index.html", context={"positions": posotions})
