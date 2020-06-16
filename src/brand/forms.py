from django import forms


class SignUpForm(forms.ModelForm):
    class Meta:
        fields = {
            "first_name",
            "last_name",
            "e-mail",
            "password",
            "confirm_password",
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
