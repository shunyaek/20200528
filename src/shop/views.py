from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def shop_view(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    context = {
        'object': obj,
    }
    return render(request, 'shop.html', context)
