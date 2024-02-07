from django.contrib import admin
from .models import Cart, CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'cart', 'created', 'updated', 'is_active']
    list_editable = ('is_active', )
    search_fields = ('product', )
    list_filter = ('product', 'cart')