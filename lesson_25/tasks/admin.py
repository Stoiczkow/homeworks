from django.contrib import admin

from .models import (
    Author,
    Book,
    EmailNotification,
    LogEntry,
    Note,
    Product,
    ScrapedPage,
    Task,
    UploadedImage,
    UserReport,
)


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(EmailNotification)
admin.site.register(LogEntry)
admin.site.register(Note)
admin.site.register(Product)
admin.site.register(ScrapedPage)
admin.site.register(Task)
admin.site.register(UploadedImage)
admin.site.register(UserReport)
