from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=100)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name


class Product(models.Model):
	category = models.ForeignKey(
		Category,
		on_delete=models.CASCADE,
		related_name='products',
		blank=True,
		null=True,
	)
	name = models.CharField(max_length=100)
	description = models.TextField()
	price = models.DecimalField(max_digits=6, decimal_places=2)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name


class Note(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()

	class Meta:
		ordering = ['id']

	def __str__(self):
		return self.title
