from django.contrib import admin
from .models import Ogloszenia

# Register your models here.

#admin.site.register(Ogloszenia)

@admin.register(Ogloszenia)
class OgloszeniaAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "created_at"]