from typing import List
from ninja import ModelSchema
from apps.common import models


class RegionSchema(ModelSchema):
    class Meta:
        model = models.Region
        fields = ["id", "title"]


class TagSchema(ModelSchema):
    class Config:
        model = models.Tag
        model_fields = ["id", "title"]


class PostSchema(ModelSchema):
    tag: List[TagSchema]

    class Config:
        model = models.Post
        model_fields = ["image", "title", "short_description", "content", "tag"]


class EventSchema(ModelSchema):
    class Meta:
        model = models.Event
        fields = ["id", "title", "is_active", "image"]


class PositionSchema(ModelSchema):
    region: RegionSchema
    event: EventSchema

    class Meta:
        model = models.Position
        fields = [
            "title",
            "description",
            "thumbnail",
            "location",
            "latitude",
            "longitude",
            "start_time",
            "arentir",
        ]
