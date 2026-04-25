from django.contrib import admin
from .models import Ogloszenie, Category

@admin.register(Ogloszenie)
class OgloszenieAdmin(admin.ModelAdmin):
    list_display = ["tytul", "cena", "data_dodania", "category"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]