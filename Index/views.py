from dataclasses import dataclass
from re import M
from django.shortcuts import get_object_or_404, render
from django.http import *
from .models import *

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def post(request):
    post = Post.objects.all()
    data = {
        'post': post
    }
    return render(request, 'posts.html', data)

def show_post(request, post_slug):
    post = get_object_or_404(Post, slug = post_slug)

    data = {
        'post': post
    }

    return render(request, 'post_single.html', data)