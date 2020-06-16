from django import forms
from .models import Product


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {
            "title",
            "summary",
            "description",
            "price",
            "images" "discount_availability",
            "discount",
            "availability_status",
            "featured",
        }


class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {
            "title",
            "summary",
            "description",
            "price",
            "images" "discount_availability",
            "discount",
            "availability_status",
            "featured",
        }


class DeleteProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {
            "confirmation",
        }
