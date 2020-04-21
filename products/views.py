from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Product

class ProductListView(LoginRequiredMixin, ListView):
	model = Product
	context_object_name = 'product_list'
	template_name = 'product/product_list.html'
	login_url = 'account_login'

class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
	model = Product
	context_object_name = 'product'
	template_name = 'product/product_detail.html'
	login_url = 'account_login'
	permission_required = 'product.special_status'
