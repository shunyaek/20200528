from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.http import JsonResponse
from csp.decorators import csp_exempt

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

import stripe
import json

from .models import Product
from .forms import ProductForm
from .forms import ProductImageForm
from .forms import CategoryForm

API_KEY = settings.STRIPE_SECRET_KEY



def checkout_view(request):
    payment_amount = 4999
    context = {
        "payment_amount": payment_amount,
    }
    response = render(request, "checkout.html", context)
    response._csp_exempt = True
    return response



def create_payment_intent_view(request):

    if request.method == "POST":
        stripe.api_key = API_KEY
        try:
            data = json.loads(request.data)
            intent = stripe.PaymentIntent.create(
                amount=500,
                currency="inr",
                metadata={"integration_check": "accept_a_payment"},
            )

            response = JsonResponse({"clientSecret": intent.client_secret})
            response._csp_exempt = True
            return response

        except Exception as e:
            response = JsonResponse({"error": str(e)}, status=403)
            response._csp_exempt = True
            return response


def payment_complete_view(request):
    return render(request, "payment-complete.html")


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
    if request.method == "POST":
        create_product_form = ProductForm(request.POST, request.FILES)
        create_product_image_form = ProductImageForm(request.POST, request.FILES)
        create_category_form = CategoryForm(request.POST, request.FILES)
        if create_product_form.is_valid() & create_product_image_form.is_valid() & create_category_form.is_valid() :
            create_product_form.save()
            create_product_image_form.save()
            create_category_form.save()
            create_product_form = ProductForm()
            create_product_image_form = ProductImageForm()
            create_category_form = CategoryForm()

    else:
        create_product_form = ProductForm()
        create_product_image_form = ProductImageForm()
        create_category_form = CategoryForm()
    context = {
        "create_product_form": create_product_form,
        "create_product_image_form": create_product_image_form,
        "create_category_form": create_category_form,
        "page_heading": "Create a new product",
        "button_value": "Create",
    }

    return render(request, "create_product.html", context)


def update_product_view(request, pk, *args, **kwargs):
    product_object = get_object_or_404(Product, pk=pk)
    update_product_form = ProductForm(request.POST and request.FILES, instance=product_object)
    if update_product_form.is_valid():
        update_product_form.save()
        update_product_form = ProductForm()

    context = {
        "update_product_form": update_product_form,
        "page_heading": "Update a product",
        "button_value": "Update",
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
