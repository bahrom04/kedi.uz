from django import forms
from .models import LostAnimal


class LostAnimalForm(forms.ModelForm):
    class Meta:
        model = LostAnimal
        fields = [
            "title",
            "description",
            "animal_type",
            "gender_type",
            "location",
            "phone_number",
            "photo",
            "latitude",
            "longitude",
            "date_lost",
        ]
