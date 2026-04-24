from django.shortcuts import render
from django.http import HttpResponse
from .models import Ogloszenie, Category


def info_view(request):
    context = {
        "naglowek": "Informacje o Browarze Wrowar Brewing",
        "opis": "Browar w Jelczu-Laskowicach, założony przez przyjaciół z   Wrocławia by warzyć dla Was najlepsze piwo.",
        "piwa": [
            "Aloha: Juicy Sour z Ananasem",
            "Reinkarnacja: Black IPA",
            "Kooperacja: Rice Cold IPA",
            "Król Piór: Dark Strong Lager",
            "Bezczelne: Lichtenhainer",
        ],
    }
    return render(request, "info.html", context)

def user_profile_view(request, username):
    return HttpResponse(f"Witaj na profilu, {username}!")

def category_list_view(request):
    categories = Category.objects.all()

    context = {
        "categories": categories
    }

    return render(request, "ogloszenia/category_list.html", context)

