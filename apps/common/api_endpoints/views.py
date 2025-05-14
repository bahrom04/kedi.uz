from typing import List, Annotated
from ninja import NinjaAPI
from apps.common import models
from apps.common.api_endpoints import schemas

api = NinjaAPI()


@api.get("/post/all", response=List[schemas.PostSchema])
def get_post_all(request):
    queryset = models.Post.objects.prefetch_related("tag").all()
    return queryset


@api.get("/position/all", response=Annotated[List[schemas.PositionSchema], 200])
def get_position_all(request):
    queryset = models.Position.objects.select_related("region", "event").all()
    return list(queryset)
