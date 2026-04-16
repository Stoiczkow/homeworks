from django.db.models import Q
from django.shortcuts import render
from .models import Post
from .forms import SearchForm

# Create your views here.

def posts_from_category(request, category_id):
    posts = Post.objects.filter(category=category_id)
    
    return render(request, "blog/category_detail.html", {
        'posts': posts
    })
    
def home(request):
    posts = Post.objects.order_by("-published_date")
    
    form = SearchForm(request.GET or None)

    if form.is_valid():
        phrase = form.cleaned_data.get('phrase')

        if phrase:
            posts = posts.filter( Q(title__icontains=phrase)| 
                                 Q(content__icontains=phrase))
    
    return render(request, 'blog/home.html', {
        'posts': posts,
        'form': form
    })
    
def profile_view(request):
    return render(request, 'account/profile.html')