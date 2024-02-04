from django.contrib import admin

from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'stock', 'category', 'created', 'updated', 'is_available']
    prepopulated_fields = {'slug':('product_name', )}
    search_fields = ['product_name']
    list_filter = ('category', )
    ordering = ('-created', )