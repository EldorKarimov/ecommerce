from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

def store(request, category_slug = None):
    if category_slug != None:
        category = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(is_available = True, category = category)
        product_count = products.count()
    else:
        products = Product.objects.filter(is_available = True)
        product_count = products.count()
    context = {
        'products':products,
        'product_count':product_count
    }
    return render(request, 'store/store.html', context)

def productDetail(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug = category_slug, slug = product_slug)
    except Exception as e:
        raise f"xatolik {e}"
    context = {
        'product':product
    }
    return render(request, 'store/product_detail.html', context)