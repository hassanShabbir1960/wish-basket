from django.contrib import admin
from django.contrib import admin
from .models import Product
from .forms import ProductForm

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    def save_model(self, request, obj, form, change):
        if 'upload_image' in form.cleaned_data:
            obj.image = form.cleaned_data['upload_image']
        super().save_model(request, obj, form, change)

admin.site.register(Product, ProductAdmin)
