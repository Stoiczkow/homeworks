from django.contrib import admin, messages
from .models import Car, Dealer
from django.utils.html import format_html
# Register your models here.

# admin.site.register(Car)

class CarInline(admin.TabularInline):
    model = Car
    extra = 1

@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
     inlines = [CarInline]

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("display_photo" ,"full_name" ,"brand", "model", "year", "price", "is_available")
    search_fields = ("brand", "model")
    list_filter = ("year", "price")
    ordering = ("-year",)

    actions = ['mark_as_unavailable']

    

    def full_name(self, obj):
        return f"{obj.brand} {obj.model}"
    
    full_name.short_description = "Pelna nazwa"

    def get_readonly_fields(self, request, obj = None):
        if obj:
            return ("year",)
        return()
    
    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="100" />',obj.photo.url)
        return "Brak zdjęcia"
    display_photo.short_description = 'Zdjęcie'
    
    def mark_as_unavailable(self, request, queryset):
        rows_updated = queryset.update(is_available = False)

        self.message_user(request, f"{rows_updated} Samochody zmienily status na niedostepne.", messages.SUCCESS)
    mark_as_unavailable.short_description = "wybierz samochody ktore maja byc niedostepne"

