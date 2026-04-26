from django.contrib import admin, messages
from django.utils.html import format_html
from .models import Car, Dealer


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("display_photo", "full_name", "brand", "model", "year", "is_available")
    search_fields = ("brand", "model")
    list_filter = ("is_available", "year")
    ordering = ("-year",)
    readonly_fields = ("year",)
    actions = ["marks_as_unavailable"]

    def full_name(self, obj):
        return f"{obj.brand} {obj.model}"
    
    full_name.short_description = "Pełna nazwa"

    def marks_as_unavailable(self, request, queryset):
        updated= queryset.update(is_available=False)
        self.message_user(
            request,
            f"{updated} samochodów oznaczono jako niedostępne",
            messages.SUCCESS
        )
    marks_as_unavailable.short_description = "Oznacz jako niedostępne"

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="150" />', obj.photo.url)
        return "Brak zdjęcia"
    display_photo.short_description = "Zdjęcie"

class CarInLine(admin.TabularInline):
    model = Car
    extra = 1

@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ("name", "address")
    inlines = [CarInLine]