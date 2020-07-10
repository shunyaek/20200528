from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import SearchForm, SignUpForm
from blog.models import BlogPost
from shop.models import Product


def search_view(request):

    if request.method == "GET":
        query = request.GET.get("q")
        blogpost_list = BlogPost.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

        product_list = Product.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

        context = {
            "product_list": product_list,
            "blogpost_list": blogpost_list,
        }

        return render(request, "search.html", context)


def index_view(request, *args, **kwargs):

    search_form = SearchForm(request.GET or None)

    if search_form.is_valid():
        search_form.save()
        search_form = SearchForm(request.GET or None)

    context = {
        "index_active_state": "active",
        "search_form": search_form,
    }
    return render(request, "index.html", context)


def sign_up_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = SignUpForm()
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(
                    request, "Welcome, %s! You have successfully registered!" % user
                )
                return redirect("brand:sign_in")
        context = {
            "form": form,
            "page_heading": "Sign-Up",
            "button_value": "Sign-Up",
        }
        return render(request, "account/sign_up.html", context)


def sign_in_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.info(request, "Username or password incorrect!")

        context = {
            "page_heading": "Sign-In",
            "button_value": "Sign-In",
        }

        return render(request, "account/sign_in.html", context)


@login_required(login_url="brand:sign_in")
def sign_out_view(request, *args, **kwargs):
    logout(request)
    return redirect("brand:sign_in")
