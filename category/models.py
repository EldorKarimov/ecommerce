from django.db import models

from shared.models import BaseModel

class Category(BaseModel):
    category_name = models.CharField(max_length = 150)
    slug = models.CharField(max_length = 150, unique = True)
    description = models.TextField()
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name