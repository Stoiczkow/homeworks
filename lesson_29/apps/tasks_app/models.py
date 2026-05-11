from django.db import models


# Z10: model maila do wysylki
class EmailNotification(models.Model):
    recipient_email = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'EmailNotification(id={self.pk}, to={self.recipient_email}, sent={self.sent_at is not None})'


# Z12: wpisy logow do okresowego czyszczenia
class LogEntry(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'LogEntry({self.created_at:%Y-%m-%d %H:%M}: {self.message})'


# Z13: zapisane tytuly stron z web scrapingu
class ScrapedPage(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=500)
    scraped_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-scraped_at']

    def __str__(self):
        return f'ScrapedPage({self.url} -> "{self.title}")'


# Z16: obrazki do klasyfikacji
class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    classification_result = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'UploadedImage(id={self.pk}, result="{self.classification_result}")'