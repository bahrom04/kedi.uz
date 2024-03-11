from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.users.models import User


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize HTML attributes for form fields
        self.fields["email"].widget.attrs.update(
            {"class": "form-email", "placeholder": "Enter email"}
        )
        self.fields["username"].widget.attrs.update(
            {"class": "form-username", "placeholder": "Enter username"}
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "form-password1", "placeholder": "Enter password"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-password2", "placeholder": "Confirm password"}
        )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email", "username", "password1", "password2")
