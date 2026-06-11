from django.views.generic import ListView

from articles.models import Category

# Zadanie 1 – Nowy model Category
class CategoryListView(ListView):
    model = Category
    template_name = 'articles/category_list.html'
    context_object_name = 'categories'
