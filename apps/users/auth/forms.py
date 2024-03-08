from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.users.models import User


class CustomUserCreationForm(UserCreationForm):
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True  # Set is_staff to True for staff users
        if commit:
            user.save()
        return user

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "username", "password1", "password2")
