from django.http import HttpResponse
from django.shortcuts import render

from .models import Product
from .forms import ProductForm


def shop_view(request, *args, **kwargs):
    products_list = Product.objects.all()
    context = {
        "products_list": products_list,
    }
    return render(request, "shop.html", context)


def create_product_view(request, *args, **kwargs):
    create_product_form = ProductForm(request.POST or None)
    if create_product_form.is_valid():
        create_product_form.save()
        create_product_form = ProductForm(request.POST or None)

    context = {
        "create_product_form": create_product_form,
    }

    return render(request, "create_product.html", context)
