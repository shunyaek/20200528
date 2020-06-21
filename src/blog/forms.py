from django import forms
from django.forms.utils import ErrorList

from .models import BlogPost


class BlogPostForm(forms.ModelForm):

    title = forms.CharField(
        label="Title",
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "(max 128 characters)", "class": "title-field"}
        ),
    )

    image = forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput(attrs={"class": "image-field"}),
        required=False,
    )

    content = forms.CharField(
        label="Content",
        required=True,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Write down the blog post content here...",
                "class": "content-field",
            }
        ),
    )

    featured = forms.BooleanField(
        label="Featured",
        initial=False,
        widget=forms.CheckboxInput(attrs={"class": "featured-field"}),
        required=False,
    )

    field_order = [
        "title",
        "image",
        "content",
        "featured",
    ]

    class Meta:
        model = BlogPost
        fields = {
            "title",
            "image",
            "content",
            "featured",
        }
