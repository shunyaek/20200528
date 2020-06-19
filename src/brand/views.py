from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from .forms import SearchForm


def search_view(request, *args, **kwargs):
    search_form = SearchForm(request.POST or None)
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


def create_user(request, *args, **kwargs):
    pass
