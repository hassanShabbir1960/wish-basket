from django.db import models

# Create your models here

import uuid

from users.models import User
from products.models import Product

class Wishlist(models.Model):
    name = models.CharField(max_length=100,default='undefined')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    products = models.ManyToManyField(Product, related_name='products_list')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
