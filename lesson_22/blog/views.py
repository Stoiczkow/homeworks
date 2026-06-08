from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import SearchForm

# Create your views here.


def home_blog(request):

    posts = Post.objects.order_by("-published_date")[0:5]

    searched_posts = None

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_text = form.cleaned_data['search_text']
            searched_posts = Post.objects.filter(Q(title__icontains=search_text)|Q(content__icontains=search_text))
    else:
        form = SearchForm()

    return render(request, "blog/index.html", {"posts": posts, "form": form, "searched": searched_posts})

def posts_in_category_list(request, category_id):

    posts = Post.objects.filter(category_id=category_id)
    return render(request, "blog/category.html", {"posts": posts,
                                                "category_id": category_id})

@login_required
def only_for_logged_in(request):
    return render(request, 'blog/personal_panel.html')