from datetime import timedelta

from django.db import models
from django.utils import timezone


class Category(models.Model):
	name = models.CharField(max_length=100)

	class Meta:
		ordering = ['name']
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name


class Article(models.Model):
	category = models.ForeignKey(
		Category,
		on_delete=models.CASCADE,
		related_name='articles',
	)
	title = models.CharField(max_length=200)
	content = models.TextField()
	pub_date = models.DateTimeField(auto_now_add=True)
	is_published = models.BooleanField(default=True)

	class Meta:
		ordering = ['-pub_date', 'title']

	def __str__(self):
		return self.title

	@property
	def is_new(self):
		return timezone.now() - self.pub_date <= timedelta(days=3)
