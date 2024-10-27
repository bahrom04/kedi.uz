from datetime import timezone
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from apps.common import models as common

class Community(common.BaseModel):
    image = models.ImageField(upload_to="community/")
    title = models.CharField(_("Title"), max_length=128)
    description = models.TextField(_("Description"), blank=True, null=True)

    telegram_link = models.URLField()



class GenderType(common.BaseModel):
    title = models.CharField(_("Title"), max_length=32)

class AnimalType(common.BaseModel):
    title = models.CharField(_("Title"), max_length=32)

class LostAnimal(common.BaseModel):
    photo = models.ImageField(upload_to='lost_animals/')
    title = models.CharField(max_length=128)
    description = models.TextField()
    animal_type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)
    gender_type = models.ForeignKey(GenderType, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)

    latitude = models.FloatField(verbose_name=_("latitude"), null=True, blank=True)
    longitude = models.FloatField(verbose_name=_("longitude"), null=True, blank=True)
    date_lost = models.DateField(null=True, blank=True)

    phone_number = models.CharField(max_length=32) 
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

   

    

    