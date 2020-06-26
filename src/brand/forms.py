from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    username = forms.CharField(
        label="Username",
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "username-field",}
        ),
    )

    first_name = forms.CharField(
        label="First name",
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "First name", "class": "first_name-field",}
        ),
    )

    last_name = forms.CharField(
        label="Last name",
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Last name", "class": "last_name-field",}
        ),
    )

    email = forms.CharField(
        label="Email",
        required=True,
        widget=forms.EmailInput(
            attrs={"placeholder": "Email", "class": "email-field",}
        ),
    )

    password1 = forms.CharField(
        label="Password1",
        required=True,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Enter password", "class": "password-field",}
        ),
    )

    password2 = forms.CharField(
        label="Password2",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm password",
                "class": "confirm_password-field",
            }
        ),
    )

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
