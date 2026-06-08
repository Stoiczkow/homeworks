from django.contrib import admin

from .models import Post, Category, Tag, PostTag

admin.site.register(Tag)
admin.site.register(PostTag)

class PostInLine(admin.TabularInline):
    model = Post
    extra = 1
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name', )
    search_fields = ('name', )
    inlines = [PostInLine]

    actions = ['make_published']

    def make_published(self, request, queryset):
        for category in queryset:
            print(category)
    

class PostTagInline(admin.TabularInline):
    model = PostTag
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostTagInline]