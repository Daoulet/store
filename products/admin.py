from django.contrib import admin
from .models import Product, Review

class ReviewInline(admin.TabularInline):
    model = Review


class ProductAdmin(admin.ModelAdmin):
	onlines = [
		ReviewInline,
	]
	list_display = ("title", "author", "price",)

admin.site.register(Product, ProductAdmin)

admin.site.register(Review)