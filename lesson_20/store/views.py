from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductForm
from .models import Category, Note, Product


def info(request):
    return HttpResponse("Informacje o stronie")


def rules(request):
    return HttpResponse("Regulamin")


def user_profile(request, username):
    return HttpResponse(f"Witaj na profilu, {username}!")


def product_list(request):
    products = Product.objects.select_related("category").order_by("name")
    return render(request, "store/product_list.html", {"products": products})


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()

    return render(request, "store/product_form.html", {"form": form})


def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.order_by("name")
    return render(
        request,
        "store/product_list.html",
        {"category": category, "products": products},
    )


def note_list(request):
    paginator = Paginator(Note.objects.order_by("id"), 3)
    page = request.GET.get("page")
    notes = paginator.get_page(page)
    return render(request, "store/note_list.html", {"notes": notes})


def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, "store/note_detail.html", {"note": note})
