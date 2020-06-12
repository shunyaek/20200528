from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def shop_view(request, *args, **kwargs):
    products_list = Product.objects.all()
    context = {
        'products_list': products_list,
    }
    return render(request, 'shop.html', context)
