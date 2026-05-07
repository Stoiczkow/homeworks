from django.shortcuts import render
from django.db import connection
from django.db.models import Q

from .models import Post
from .forms import SearchForm

# Create your views here.

def home_blog(request):

    posts = Post.objects.order_by("-published_date")[0:5]

    form = SearchForm(request.POST)
    searched_posts = None

    if request.method == 'POST':    
        if form.is_valid():
            search_text = form.cleaned_data['search_text']
            print(search_text)
            searched_posts = Post.objects.filter(Q(title__icontains=search_text)|Q(content__icontains=search_text))
            print(searched_posts)

    return render(request, "blog/index.html", {"posts": posts, "form": form, "searched": searched_posts})

def posts_in_category_list(request, category_id):

    posts = Post.objects.filter(category_id=category_id)

    return render(request, "blog/category.html", {"posts": posts,
                                                "category_id": category_id})