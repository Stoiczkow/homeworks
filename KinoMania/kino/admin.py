from django.contrib import admin
from .models import Gatunek, Aktor, Rezyser, Film, Seans, Rezerwacja


@admin.register(Gatunek)
class GatunekAdmin(admin.ModelAdmin):
    list_display = ('nazwa',)
    search_fields = ('nazwa',)


@admin.register(Aktor)
class AktorAdmin(admin.ModelAdmin):
    list_display = ('imie_nazwisko', 'zdjecie_preview')
    search_fields = ('imie_nazwisko',)
    readonly_fields = ('zdjecie_preview',)

    def zdjecie_preview(self, obj):
        if obj.zdjecie:
            return f'<img src="{obj.zdjecie.url}" width="50" height="75" />'
        return 'Brak zdjęcia'
    zdjecie_preview.allow_tags = True


@admin.register(Rezyser)
class RezyserAdmin(admin.ModelAdmin):
    list_display = ('imie_nazwisko', 'zdjecie_preview')
    search_fields = ('imie_nazwisko',)
    readonly_fields = ('zdjecie_preview',)

    def zdjecie_preview(self, obj):
        if obj.zdjecie:
            return f'<img src="{obj.zdjecie.url}" width="50" height="75" />'
        return 'Brak zdjęcia'
    zdjecie_preview.allow_tags = True


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('tytul', 'data_premiery', 'rezyser', 'plakat_preview')
    list_filter = ('data_premiery', 'gatunek', 'rezyser')
    search_fields = ('tytul', 'opis')
    filter_horizontal = ('gatunek', 'aktorzy')
    readonly_fields = ('data_dodania', 'plakat_preview')
    
    fieldsets = (
        ('Podstawowe informacje', {
            'fields': ('tytul', 'opis', 'data_premiery')
        }),
        ('Multimedia', {
            'fields': ('plakat', 'plakat_preview')
        }),
        ('Relacje', {
            'fields': ('rezyser', 'aktorzy', 'gatunek')
        }),
        ('Metadane', {
            'fields': ('data_dodania',),
            'classes': ('collapse',)
        }),
    )

    def plakat_preview(self, obj):
        if obj.plakat:
            return f'<img src="{obj.plakat.url}" width="100" height="150" />'
        return 'Brak plakatu'
    plakat_preview.allow_tags = True


@admin.register(Seans)
class SeansAdmin(admin.ModelAdmin):
    list_display = ('film', 'czas_rozpoczecia', 'cena', 'dostepne_miejsca', 'liczba_miejsc')
    list_filter = ('czas_rozpoczecia', 'film', 'cena')
    search_fields = ('film__tytul',)
    readonly_fields = ('dostepne_miejsca',)
    
    fieldsets = (
        ('Film', {
            'fields': ('film',)
        }),
        ('Szczegóły seansu', {
            'fields': ('czas_rozpoczecia', 'cena', 'liczba_miejsc', 'dostepne_miejsca')
        }),
    )


@admin.register(Rezerwacja)
class RezerwacjaAdmin(admin.ModelAdmin):
    list_display = ('id', 'uzytkownik', 'seans', 'ilosc_miejsc', 'status', 'data_rezerwacji')
    list_filter = ('status', 'data_rezerwacji', 'seans__czas_rozpoczecia')
    search_fields = ('uzytkownik__username', 'seans__film__tytul')
    readonly_fields = ('data_rezerwacji', 'data_modificacji')
    
    fieldsets = (
        ('Użytkownik i seans', {
            'fields': ('uzytkownik', 'seans')
        }),
        ('Szczegóły rezerwacji', {
            'fields': ('ilosc_miejsc', 'status')
        }),
        ('Daty', {
            'fields': ('data_rezerwacji', 'data_modificacji'),
            'classes': ('collapse',)
        }),
    )

    actions = ['potwierdz_rezerwacje', 'anuluj_rezerwacje']

    def potwierdz_rezerwacje(self, request, queryset):
        updated = 0
        for rez in queryset.filter(status='pending'):
            rez.confirm()
            updated += 1
        self.message_user(request, f'Potwierdzone {updated} rezerwacji.')
    potwierdz_rezerwacje.short_description = "Potwierdź zaznaczone rezerwacje"

    def anuluj_rezerwacje(self, request, queryset):
        updated = 0
        for rez in queryset.exclude(status='cancelled'):
            rez.cancel()
            updated += 1
        self.message_user(request, f'Anulowano {updated} rezerwacji.')
    anuluj_rezerwacje.short_description = "Anuluj zaznaczone rezerwacje"

