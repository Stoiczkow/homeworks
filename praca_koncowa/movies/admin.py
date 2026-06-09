from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import Movie, Actor, Genre, Director

# admin.site.register(Movie)
admin.site.register(Actor)
# admin.site.register(Genre)
# admin.site.register(Director)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'display_photo','content', 'release_date', 'director')

    list_filter = ('genre', 'release_date')
    search_fields = ('title',) #'director')
    ordering = ('-release_date',)
    filter_horizontal = ('actor', 'genre')
    search_help_text = "Podaj szukanego tytulu, rezysera, actora"

    def display_photo(self, obj):
        if obj.poster:
            return format_html('<img src="{}" width="100" />',
        obj.poster.url)
        return "Brak zdjęcia"
    
    display_photo.short_description = 'Zdjęcie'


class MovieInLine(admin.TabularInline):
    model = Movie
    extra = 1
    fields = ('title', 'release_date',)


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    inlines = [MovieInLine]
    list_display = ("photogrphy","name_surname")
    search_fields = ("name_surname",)


    def photogrphy(self, object):
        if object.actor_image:
            return format_html('<img src="{}" width="150" />',
        object.actor_image.url)
        return "Brak fotography"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ["genre_name"]
