from rest_framework import serializers
from wishlist.models import Wishlist
from users.models import User
from products.models import Product


class WishlistSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Wishlist
        fields = ['name','id', 'products', 'user']

    def validate_products(self, value):
        """Ensure the products list is not empty."""
        if not value:
            raise serializers.ValidationError("This field may not be empty.")
        return value

