from typing import List
from ninja import NinjaAPI
from apps.common import models
from apps.common.api_endpoints import schemas

api = NinjaAPI()


@api.get("/posts", response=List[schemas.PostOut])
def posts(request):
    queryset = models.Post.objects.prefetch_related("tag").all()
    return queryset



