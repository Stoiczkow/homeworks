from django.contrib import admin
from .models import Article, Author, Category, Tag


class ArticleTabularInline(admin.TabularInline):
    model = Article
    extra = 1


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    inlines = [ArticleTabularInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.action(description='Zmien status na opublikowany')
def make_published(modeladmin, request, queryset):
    queryset.update(status='published')


@admin.action(description='Zmien status na szkic')
def make_draft(modeladmin, request, queryset):
    queryset.update(status='draft')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    actions = [make_published, make_draft]
    list_display = ('title', 'author_id', 'category_id', 'status', 'published_date', 'short_content', 'tag_list')
    list_filter = ('status', 'category_id')
    search_fields = ('title', 'content')
    filter_horizontal = ('tags',)
    date_hierarchy = 'published_date'

    @admin.display(description='Zajawka')
    def short_content(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content

    @admin.display(description='Tagi')
    def tag_list(self, obj):
        return ', '.join(tag.name for tag in obj.tags.all())
