from django.views.generic import ListView, DetailView

from .models import Category, Article


# Zadanie 3 – lista kategorii
class CategoryListView(ListView):
    model = Category
    template_name = 'blog/category_list.html'
    context_object_name = 'categories'


# Zadanie 6 – szczegóły kategorii (+ zadanie 7: lista artykułów)
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'blog/category_detail.html'
    context_object_name = 'category'


# Zadanie 8 + 10 – lista artykułów (tylko opublikowane + wyszukiwanie)
class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        queryset = Article.objects.filter(is_published=True)
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(title__icontains=q)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context