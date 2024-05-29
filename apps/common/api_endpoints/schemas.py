from typing import List
from ninja import ModelSchema
from apps.common import models


class TagOut(ModelSchema):
    class Config:
        model = models.Tag
        model_fields = ["id", "title"]


class PostOut(ModelSchema):
    tag: List[TagOut]

    class Config:
        model = models.Post
        model_fields = ["image", "title", "short_description", "content", "tag"]
