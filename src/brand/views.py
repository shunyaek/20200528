from django.http import HttpResponse
from django.shortcuts import render

from .forms import SearchForm


def search_view(request, *args, **kwargs):
    search_form = SearchForm(request.POST or None)
    if search_form.is_valid():
        search_form.save()
        search_form = SearchForm(request.POST or None)

    context = {
        'search_form': search_form,
    }

    return render(request, "search.html", context)


def index_view(request, *args, **kwargs):
    context = {}
    return render(request, "index.html", context)
