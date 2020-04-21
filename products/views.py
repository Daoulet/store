from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Product
from django.db.models import Q

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

class SearchResultsListView(ListView):
	model = Product
	context_object_name = 'product_list'
	template_name = 'product/search_results.html'

	def get_queryset(self):
		query = self.request.GET.get('q')
		return Product.objects.filter(
			Q(title__icontains=query) | Q(title__icontains=query)
			
		)