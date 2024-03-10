from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.users.models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "username", "password1", "password2")
