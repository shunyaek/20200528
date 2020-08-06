from django import forms

from .models import Product
from .models import Customer
from .models import Category
from .models import ProductImage


class ProductForm(forms.ModelForm):
    
    title = forms.CharField(
        label="Title",
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "(max 128 characters)", "class": "title-field"}
        ),
    )

    description = forms.CharField(
        label="Description",
        widget=forms.Textarea(
            attrs={
                "placeholder": "Write down the product description here",
                "class": "description-field",
            }
        ),
    )

    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    images = forms.ModelMultipleChoiceField(queryset=ProductImage.objects.all())
    
    price = forms.DecimalField(
        label="Price",
        required=True,
        widget=forms.NumberInput(
            attrs={"class": "price-field"}
        ),
    )

    discount_availability = forms.BooleanField(
        label="Discount Availability",
        widget=forms.CheckboxInput(attrs={"class": "discount_availability-field"}),
        required=False,
    )

    discount = forms.IntegerField(
        label="Discount",
        widget=forms.NumberInput(attrs={"class": "discount-field"}),
        required=False,
    )

    availability = forms.BooleanField(
        label="Availability",
        widget=forms.CheckboxInput(attrs={"class": "availability-field"}),
        required=True,
    )

    featured = forms.BooleanField(
        label="Featured",
        initial=False,
        widget=forms.CheckboxInput(attrs={"class": "featured-field"}),
        required=True,
    )

    field_order = [
        "title",
        "description",
        "category",
        "image",
        "price",
        "discount_availability",
        "discount",
        "availability",
        "featured",
    ]

    class Meta:
        model = Product
        model = Customer
        model = Category
        model = ProductImage
        fields = {
            "title",
            "description",
            "category",
            "image",
            "price",
            "discount_availability",
            "discount",
            "availability",
            "featured",
        }


class ProductImageForm(forms.ModelForm):
    title = forms.CharField(
        label="Image Title",
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Write down the title of an Image",
                "class": "title-field",
            }
        )
    )

    image = forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput(attrs={"class": "image-field"}),
        required=False,
    )

    field_order = [
        "title",
        "image",
    ]

    class Meta:
        model = ProductImage
        fields = {
            "title",
            "image",
        }

class CategoryForm(forms.ModelForm):
    title = forms.CharField(
        label="Category",
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Write down the category of product",
                "class": "title-field",
            }
        )
    )

    field_order = [
        "title",
    ]

    class Meta:
        model = Category
        fields = {
            "title",
        }

