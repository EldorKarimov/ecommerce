from django.db import models
from shared.models import BaseModel
from category.models import Category
from django.urls import reverse

class Product(BaseModel):
    product_name = models.CharField(max_length = 50, unique = True)
    slug = models.SlugField(max_length = 50, unique = True)
    description = models.TextField(blank = True)
    price = models.PositiveBigIntegerField()
    image = models.ImageField(upload_to='photos/product')
    stock = models.PositiveBigIntegerField()
    is_available = models.BooleanField(default = False)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.product_name
    
    def get_url(self):
        return reverse('store:detail', args=[self.category.slug, self.slug])