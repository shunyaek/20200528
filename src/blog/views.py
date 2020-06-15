from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def blog_view(request, *args, **kwargs):
    blog_posts = Post.objects.all()
    context = {
        'blog_posts': blog_posts,
    }
    return render(request, 'blog.html', context)
