from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from .serializers import ProductSerializer

def get_products(request,category=None):
    if category:
        ## When a category is specified in URL
        products = Product.objects.filter(category=category)
    else:
        ## When no category is specified, return all products
        products = Product.objects.all()

    serializer = ProductSerializer(products, many=True)
    return JsonResponse({
                        "products": serializer.data
                        })

