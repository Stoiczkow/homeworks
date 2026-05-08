from django.contrib import admin, messages
from django.utils.html import format_html

from .models import Car, Dealer


class CarInline(admin.TabularInline):
    model = Car
    extra = 0


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ("name", "address")
    search_fields = ("name", "address")
    inlines = [CarInline]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "thumbnail",
        "full_name",
        "brand",
        "model",
        "year",
        "is_available",
    )
    search_fields = ("brand", "model")
    list_filter = ("is_available", "year")
    ordering = ("-year",)
    readonly_fields = ("year",)
    actions = ("mark_as_unavailable",)

    def full_name(self, obj):
        return f"{obj.brand} {obj.model}"

    full_name.short_description = "Pełna nazwa"

    def thumbnail(self, obj):
        if not obj.photo:
            return "-"

        return format_html(
            '<img src="{}" width="150" alt="{} {}">',
            obj.photo.url,
            obj.brand,
            obj.model,
        )

    thumbnail.short_description = "Zdjęcie"

    @admin.action(description="Oznacz jako niedostępne")
    def mark_as_unavailable(self, request, queryset):
        updated_count = queryset.update(is_available=False)
        self.message_user(
            request,
            f"Oznaczono jako niedostępne: {updated_count}",
            messages.SUCCESS,
        )
