from django.urls import reverse_lazy
from django.views.generic import CreateView
from apps.users.models import User
from apps.users.auth.forms import CustomUserCreationForm

class UserRegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"
