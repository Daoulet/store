from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Product(models.Model):
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	cover = models.ImageField(upload_to='covers/', blank=True)

	class Meta:
		permissions = [
			('special_status', 'Can see all products'),
	]

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('product_detail', args=[str(self.id)])


class Review(models.Model):
	product = models.ForeignKey(
		Product,
		on_delete=models.CASCADE,
		related_name='reviews',
	)
	review = models.CharField(max_length=200)
	author = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE,
	)


	def __str__(self):
		return self.review