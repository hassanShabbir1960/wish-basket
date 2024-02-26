from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    upload_image = forms.ImageField(required=False, label='Image')

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'category', 'upload_image']

    def clean_upload_image(self):
        image = self.cleaned_data.get('upload_image')
        if image:
            return image.read()
        return None
