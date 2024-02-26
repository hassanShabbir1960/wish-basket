import uuid
from enum import Enum
from django.db import models

class Category(Enum):
    TECH = 'TECH'
    COOKING = 'COOKING'
    TOYS = 'TOYS'
    FASHION = 'FASHION'


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image = models.ImageField(upload_to='product_images/')
    image = models.BinaryField(null=True, blank=True)
    category = models.CharField(max_length=100, choices=[(tag.value, tag.name) for tag in Category])

    def __str__(self):
        return f'{self.name} {self.price} {self.category}'

