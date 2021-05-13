from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    # change parent properties
    class Meta:
        model = User # change user model when saving to this form
        # define the order of the fields in the form
        fields = ["username", "email", "password1", "password2"]
