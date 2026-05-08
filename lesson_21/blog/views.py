from django.shortcuts import render
from .models import Post

# Create your views here.

def category_posts(requests, category_id):
    posts = Post.objects.filter(category_id)