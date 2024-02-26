import base64
from rest_framework import serializers

class Base64BytesField(serializers.Field):
    def to_representation(self, value):
        if value:
            return base64.b64encode(value).decode('utf-8')
        return None

    def to_internal_value(self, data):
        try:
            return base64.b64decode(data)
        except ValueError as e:
            raise serializers.ValidationError('This field requires a Base64 encoded string.') from e

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    image = Base64BytesField(allow_null=True, required=False)

    class Meta:
        model = Product
        fields = '__all__'
