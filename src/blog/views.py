from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from .models import Post
from .forms import PostForm


def blog_view(request, *args, **kwargs):
    blog_posts = Post.objects.all().order_by('-publication_date')
    context = {
        "blog_posts": blog_posts,
    }
    return render(request, "blog.html", context)


def create_post_view(request, *args, **kwargs):
    form = PostForm(request.POST or None)
    form.field_order = {
        "title",
        "image",
        "content",
        "featured",
    }
    if form.is_valid():
        form.save()
        form = PostForm()
    context = {
        "form": form,
        "page_heading": "Create a blog post",
        "button_value": "Create",
    }
    return render(request, "create_post.html", context)


def read_post_view(request, pk, *args, **kwargs):
    post_object = get_object_or_404(Post, pk=pk)
    context = {
        "post": post_object,
    }
    return render(request, "post.html", context)


def update_post_view(request, pk, *args, **kwargs):
    post_object = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post_object)
    if form.is_valid():
        form.save()
    context = {
        "form": form,
        "page_heading": "Update blog post",
        "button_value": "Update",
    }
    return render(request, "create_post.html", context)


def delete_post_view(request, pk, *args, **kwargs):
    post_object = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post_object.delete()
        return redirect('../../')
    context = {
        "post": post_object,
    }
    return render(request, 'delete_post.html', context)
