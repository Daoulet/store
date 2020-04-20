from django.db import models

class Product(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=8, decimal_places=2)

	def __str__(self):
		return self.title
