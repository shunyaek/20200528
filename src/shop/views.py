from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse

import stripe
import json

from .models import Product
from .forms import ProductForm

API_KEY = settings.STRIPE_SECRET_KEY


def checkout_view(request):

    def pay():
        stripe.api_key = API_KEY
        try:
            intent = stripe.PaymentIntent.create(amount=500, currency="inr")
            return intent["client_secret"]

        except Exception as e:
            return JsonResponse(error=str(e)), 403

    context = {
        "client_secret": pay(),
        "STRIPE_PUBLISHABLE_KEY": settings.STRIPE_PUBLISHABLE_KEY,
    }

    return render(request, "checkout.html", context)

    """ if request.method == "POST":
        stripe.api_key = API_KEY
        try:
            # data = json.loads(request.data)
            intent = stripe.PaymentIntent.create(amount=500, currency="inr")

            return json.dumps({"clientSecret": intent["client_secret"]})

        except Exception as e:
            return json.dumps(error=str(e)), 403
        
        context = {
            "client_secret": intent.client_secret,
            "STRIPE_PUBLISHABLE_KEY": settings.STRIPE_PUBLISHABLE_KEY,
        }
        return render(request, "checkout.html", context) """


def shop_view(request, *args, **kwargs):
    products_list = Product.objects.all()
    context = {
        "products_list": products_list,
        "shop_active_state": "active",
    }
    return render(request, "shop.html", context)


def product_view(request, *args, **kwargs):
    context = {}
    return render(request, "product.html", context)


def create_product_view(request, *args, **kwargs):
    create_product_form = ProductForm(request.POST or None)
    if create_product_form.is_valid():
        create_product_form.save()
        create_product_form = ProductForm(request.POST or None)

    context = {
        "create_product_form": create_product_form,
    }

    return render(request, "create_product.html", context)


def update_product_view(request, *args, **kwargs):
    update_product_form = ProductForm(request.POST or None)
    if update_product_form.is_valid():
        update_product_form.save()
        update_product_form = ProductForm(request.POST or None)

    context = {
        "update_product_form": update_product_form,
    }

    return render(request, "update_product.html", context)


""" def delete_product_view(request, *args, **kwargs):
    delete_product_form = DeleteProductForm(request.POST or None)
    if delete_product_form.is_valid():
        delete_product_form.save()
        delete_product_form = DeleteProductForm(request.POST or None)

    context = {
        "delete_product_form": delete_product_form,
    }

    return render(request, "delete_product.html", context) """
