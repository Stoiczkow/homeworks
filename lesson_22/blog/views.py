from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Category, Post


def home(request):
    query = request.GET.get("q", "")
    posts = Post.objects.select_related("category").prefetch_related("tags").order_by("-created_at")

    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        posts = posts[:5]

    return render(request, "blog/home.html", {"posts": posts, "query": query})


def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category).order_by("-created_at")
    return render(request, "blog/category_posts.html", {"category": category, "posts": posts})
