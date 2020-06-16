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
            "discount_availability",
            "discount",
            "availability_status",
            "featured",
        }


class ReadProductForm(forms.ModelForm):
    pass


class UpdateProductForm(forms.ModelForm):
    pass


class DeleteProductForm(forms.ModelForm):
    pass
