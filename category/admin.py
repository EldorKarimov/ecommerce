from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'slug', 'created', 'updated')
    search_fields = ('category_name', 'slug')
    prepopulated_fields = {'slug': ('category_name',)}
    ordering = ('-created', )