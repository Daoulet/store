from django.views.generic import ListView, DetailView

from .models import Product

class ProductListView(ListView):
	model = Product
	context_object_name = 'product_list'
	template_name = 'product/product_list.html'

class ProductDetailView(DetailView):
	model = Product
	context_object_name = 'product'
	template_name = 'product/product_detail.html'
