from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post


def blog_view(request, *args, **kwargs):
    blog_posts = Post.objects.all()
    context = {
        "blog_posts": blog_posts,
    }
    return render(request, "blog.html", context)


def read_post_view(request, pk, *args, **kwargs):
    post = get_object_or_404(Post, pk=pk)
    context = {
        "post": post,
    }
    return render(request, "post.html", context)
