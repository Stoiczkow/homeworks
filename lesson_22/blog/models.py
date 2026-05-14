from django.db import models
from django.utils import timezone


class Category(models.Model):
	name = models.CharField(max_length=100, unique=True)

	class Meta:
		ordering = ['name']
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=100, unique=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name


class Post(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
	tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
	title = models.CharField(max_length=200)
	content = models.TextField()
	publication_date = models.DateTimeField(default=timezone.now)
	is_published = models.BooleanField(default=True)

	class Meta:
		ordering = ['-publication_date']

	def __str__(self):
		return self.title
