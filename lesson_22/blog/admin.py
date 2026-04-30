from django.contrib import admin

# Register your models here.
from .models import Post, Category#, Tag


admin.site.register(Category)
# admin.site.register(Tag)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_tags')

    def get_tags(self, obj):
        return ", ".join([t.name for t in obj.tags.all()])