from django.views.generic import DetailView, ListView

from articles.models import Category

# Zadanie 1 – Nowy model Category
class CategoryListView(ListView):
    model = Category
    template_name = 'articles/category_list.html'
    context_object_name = 'categories'


# Zadanie 6 – szczegóły kategorii
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'articles/category_detail.html'
    context_object_name = 'category'