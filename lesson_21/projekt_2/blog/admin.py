from django.contrib import admin

from .models import Post, Category, Tag, PostTag
from .ai_service import generate_text

# admin.site.register(Post)
# admin.site.register(Category)

class PostTagInLine(admin.TabularInline):
    model = PostTag
    extra = 1

class PostInLine(admin.TabularInline):
    model = Post
    
    extra = 1
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ("name",)
    search_fields = ("name",)
    inlines = [PostInLine]
    
    actions = ['make_published']
    def make_published(self, request, queryset):
        for category in queryset:
            print(category)
    
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published_date', 'get_tags_count')
    list_filter = ('category', 'published_date')
    search_fields = ('title', 'author', 'content')
    inlines = [PostTagInLine]

    def get_tags_count(self, obj):
        return obj.posttag_set.count()
    get_tags_count.short_description = 'Liczba tagów'

    actions = ["generate_content", "translate_to_english", "suggest_tags"]

    def generate_content(self, request, queryset):
        for obj in queryset:
            prompt = f"Napisz angażujący artykuł na bloga o tytule: '{obj.title}'. Artykuł powinien mieć około 300 słów i być napisany w języku polskim."
            obj.content = generate_text(prompt)
            obj.save()

    generate_content.short_description = "Wygeneruj treść posta"

    def translate_to_english(self, request, queryset):
        for obj in queryset:
            prompt = f"Przetłumacz poniższy tekst na język angielski (styl formalny):\n\n{obj.content}"
            eng = generate_text(prompt)
            print(eng)
            obj.content = eng
            obj.save()

    translate_to_english.short_description = "Przetłumacz na angielski"

    def suggest_tags(self, request, queryset):
        for obj in queryset:
            prompt = f"Na podstawie tytułu '{obj.title}' i treści '{obj.content}', zasugeruj 5-7 tagów. Zwróć je jako lista oddzielona przecinkami."
            obj.tags = generate_text(prompt)
            obj.save()

    suggest_tags.short_description = "Zasugeruj tagi"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_posts_count')
    search_fields = ('name',)
    
    def get_posts_count(self, obj):
        return obj.posttag_set.count()
    get_posts_count.short_description = 'Liczba postów'


@admin.register(PostTag)
class PostTagAdmin(admin.ModelAdmin):
    list_display = ('post', 'tag', 'created_at')
    list_filter = ('tag', 'created_at')
    search_fields = ('post__title', 'tag__name')