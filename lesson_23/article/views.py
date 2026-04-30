from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Article, Category
from .forms import ArticleSearchForm

def create_article(request):
    new_title = request.GET.get('title')
    new_content = request.GET.get('content')

    print(new_title)
    print(new_content)

    newarticle = Article.objects.create(
        title = new_title,
        content=new_content
    )

    return HttpResponse(f"Stworzono obiekt {newarticle.id}")



def filterArticele(request):
    query = request.GET.get('filter')
    # Pobieramy artykuły pasujące do wzorca
    articles = Article.objects.filter(title="Warszaea") 
    
    # Przekazujemy artykuły do pliku HTML w słowniku (tzw. context)
    return render(request, 'article.html', {'articles': articles})


#task3
def show_category(request):
    categories = Category.objects.all()

    return render(request, 'article/show_category.html', {'categories': categories})


#task6 i task7
def category_detail_view(request, id_category):
    try:
        object_category = Category.objects.get(id = id_category)
    except Category.DoesNotExist:
        object_category = None
        object_category = []
    
    objects = object_category.article_set.all()
    return render(request, "article/category_detail.html", {"object_category":object_category,
                                                            "objects":objects})


# task8
def show(request, id_category):
    objects = Category.objects.get(id = id_category)
    is_published_objects = objects.article_set.filter(is_published=True)

    return render(request, "article/article_list.html", {"is_published_objects" : is_published_objects})

#task 10


def article_list_view(request):

    phrase = ArticleSearchForm(request.GET)
    articles = Article.objects.all()

    if phrase.is_valid():
        query = phrase.cleaned_data.get('text')
        if query:
            articles = articles.filter(title__icontains = query)

    return render(request, "article/search_phrase.html", {"phrase" : phrase,
                                                          "articles" : articles} )





