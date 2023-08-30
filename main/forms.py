from django import forms
from django.contrib.auth.forms import UserCreationForm
from main.models import User

class RegistrForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=["email","username","password1","password2"]
