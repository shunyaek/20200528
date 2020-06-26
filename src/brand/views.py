from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .forms import SearchForm, SignUpForm
from blog.models import BlogPost
from shop.models import Product


def search_view(request, search_query, *args, **kwargs):
    search_form = SearchForm(request.POST or None)
    post_results = BlogPost.objects.all()
    # post_results = BlogPost.objects.get(title__icontains=search_query)
    if search_form.is_valid():
        search_form.save()
        search_form = SearchForm(request.POST or None)

    context = {
        "search_form": search_form,
    }

    return render(request, "search.html", context)


def index_view(request, *args, **kwargs):
    context = {
        "index_active_state": "active",
    }
    return render(request, "index.html", context)


def sign_up_view(request, *args, **kwargs):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("brand:sign_in")
    context = {
        "form": form,
        "page_heading": "Sign-Up",
        "button_value": "Sign-Up",
    }
    return render(request, "account/sign_up.html", context)


def sign_in_view(request, *args, **kwargs):
    form = UserCreationForm()
    context = {
        "form": form,
        "page_heading": "Sign-In",
        "button_value": "Sign-In",
    }
    return render(request, "account/sign_up.html", context)
