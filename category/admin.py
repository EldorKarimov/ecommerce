from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'slug', 'description', 'created', 'updated')
    search_fields = ('category_name', 'slug')
    prepopulated_fields = {'slug': ('category_name',)}
    ordering = ('-created', )

    fieldsets = (
        (None, {
            'fields': ('category_name', 'slug')
        }),
        ('Description and Image', {
            'fields': ('description', 'cat_image'),
            'classes': ('collapse',)  # This makes the fields collapsible
        }),
    )
