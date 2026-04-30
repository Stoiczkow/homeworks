from django.shortcuts import render
from .models import Post, Category
from .forms import SearchForm
from django.db.models import Q
# Create your views here.

#task2
def show_posts_category(request, id_category):
    posts = Post.objects.filter(category_id = id_category)
    category_name = Category.objects.filter(id= id_category).first()
    return render(request, "blog/show_posts.html", {"posts" : posts,
                                                    "category_name" : category_name})

#task3
def show_all(request):
    posts = Post.objects.order_by("-created_at")[:5]
    return render(request, "blog/show_all.html", {"posts" : posts})

#task6

def post_search_engine(request):
    post_phrase = SearchForm(request.GET or None)
    posts = Post.objects.all()
    
    if post_phrase.is_valid():
        query = post_phrase.cleaned_data.get('text')
        if query:
            posts = posts.filter(
                Q(title__icontains = query) | Q(description__icontains = query)
                )

    return render(request, "blog/xxx.html", {"posts" : posts,
                                             "post_phrase" : post_phrase})

