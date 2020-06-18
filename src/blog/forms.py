from django import forms
from django.forms.utils import ErrorList

from .models import Post


""" class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ""
        return '<div class="errorlist">%s</div>' % "".join(
            ['<div class="error">%s</div>' % e for e in self]
        ) """


class PostForm(forms.ModelForm):

    title = forms.CharField(
        label="Title",
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "(max 128 characters)", "class": "title-field"}
        ),
    )

    image = forms.ImageField(
        label="Image",
        allow_empty_file=True,
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
        model = Post
        fields = {
            "title",
            "image",
            "content",
            "featured",
        }
