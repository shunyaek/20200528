from django import forms


class SearchForm(forms.ModelForm):
    class Meta:
        fields = {
            "search",
        }
