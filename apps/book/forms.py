from django.utils import timezone
from django import forms
from django.utils.formats import get_format
from django.conf import settings

from .models import LostAnimal


class LostAnimalForm(forms.ModelForm):
    date_lost = forms.DateField(
        required=False,
        input_formats=settings.DATE_INPUT_FORMATS
    )
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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adjust date format based on locale
        date_format = get_format('DATE_INPUT_FORMATS')
        if date_format:
            self.fields['date_lost'].input_formats = date_format

    def clean_date_lost(self):
        date_lost = self.cleaned_data.get('date_lost')
        if date_lost and date_lost > timezone.now().date():
            raise forms.ValidationError("Date cannot be in the future")
        return date_lost
