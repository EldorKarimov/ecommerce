from django.db import models
from shared.models import BaseModel
from store.models import Product

class Cart(BaseModel):
    cart_id = models.CharField(max_length = 150)

    def __str__(self):
        return self.cart_id
    
class CartItem(BaseModel):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.product