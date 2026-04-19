from django.shortcuts import render
from django.db import connection
from django.db.models import Q
from .models import Post
from .forms import SeargeForm
# Create your views here.

def category_posts(request, category_id):

    posts = Post.objects.filter(category = category_id) #zeby uzyc  OR musimy zaimportować obkiet Q

    # zapytanie OR
    # posts = Post.objects.filter(Q(title_incontains=phrase)| Q(content_incontains=phrase))

    return render(request, "blog/category_post.html", {"posts_key": posts })



def home(request):
    # wywołanie postów od 0 do 5
    posts = Post.objects.order_by("-published_date")[0:5]


    form = SeargeForm(request.GET or None) # None usunie requriment field pole

    if form.is_valid():
        phrase  = form.cleaned_data["phrase"]
         # zapytanie OR
        posts = Post.objects.filter(Q(title__icontains=phrase)| 
                                    Q(content__icontains=phrase))
       # posts = Post.objects.filter(i)

    # list(posts)
    # print(connection.queries)
    return render(request, "blog/home.html", {"posts": posts, "form": form})