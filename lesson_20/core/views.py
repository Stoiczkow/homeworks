from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductForm
from .models import Category, Note, Product


def home_view(request):
	return redirect('product-list')


def info_view(request):
	return HttpResponse('Informacje o stronie')


def rules_view(request):
	return HttpResponse('Regulamin')


def user_profile_view(request, username):
	return HttpResponse(f'Witaj na profilu, {username}!')


def product_list_view(request):
	products = Product.objects.select_related('category').all()
	return render(
		request,
		'product_list.html',
		{
			'products': products,
			'categories': Category.objects.all(),
			'page_title': 'Lista produktów',
			'heading': 'Lista produktów',
		},
	)


def product_create_view(request):
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('product-list')
	else:
		form = ProductForm()

	return render(
		request,
		'product_form.html',
		{
			'form': form,
		},
	)


def category_products_view(request, category_id):
	category = get_object_or_404(Category, pk=category_id)
	products = Product.objects.select_related('category').filter(category=category)
	return render(
		request,
		'product_list.html',
		{
			'products': products,
			'categories': Category.objects.all(),
			'page_title': f'Produkty w kategorii: {category.name}',
			'heading': f'Kategoria: {category.name}',
			'active_category': category,
		},
	)


def note_list_view(request):
	paginator = Paginator(Note.objects.all(), 3)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	return render(
		request,
		'note_list.html',
		{
			'page_obj': page_obj,
		},
	)


def note_detail_view(request, note_id):
	note = get_object_or_404(Note, pk=note_id)
	return render(
		request,
		'note_detail.html',
		{
			'note': note,
		},
	)
