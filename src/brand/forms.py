from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    field_order = [
        "username",
        "first_name",
        "last_name",
        "email",
        "password1",
        "password2",
    ]

    class Meta:
        model = User
        fields = {
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        }


class SignInForm(forms.ModelForm):
    class Meta:
        fields = {
            "e-mail",
            "password",
        }


class SearchForm(forms.ModelForm):
    class Meta:
        fields = {
            "search",
        }
