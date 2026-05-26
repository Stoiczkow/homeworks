from django.contrib import admin
from .models import Kategoria, Produkt, Notatka, Autor, Ksiazka

admin.site.register(Kategoria)
admin.site.register(Produkt)
admin.site.register(Notatka)
admin.site.register(Autor)
admin.site.register(Ksiazka)
