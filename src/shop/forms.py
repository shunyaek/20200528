from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {
            "title",
            "summary",
            "description",
            "price",
            "discount_availability",
            "discount",
            "availability_status",
            "featured",
        }
