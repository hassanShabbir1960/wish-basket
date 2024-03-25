from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Wishlist
from products.models import Product,Category
from users.models import User  # Adjust these imports based on your actual model structure
from uuid import UUID
class WishlistAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='test@gmail.com', name='testuser', password='testpassword123')
        self.product = Product.objects.create(
            name='Test Product',
            price=10.00,
            category=Category.TOYS.value
        )
        self.wishlist_data = {
            'name': 'Test Wishlist',
            'user': self.user,
        }
        self.wishlist = Wishlist.objects.create(**self.wishlist_data)  # Adjust according to your model and fields
        self.wishlist.products.set([self.product.id])

    def test_create_wishlist_success(self):
        """
        Ensure we can create a new wishlist object.
        """

        url = reverse('wishlist-list')  # Adjust this to the correct URL name for wishlist creation
        data = {
            'user': self.user.id,
            'products': [self.product.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Wishlist.objects.count(), 2)  # Assuming one wishlist already exists from setUp

    def test_get_wishlist_success(self):
        """
        Ensure we can retrieve a wishlist.
        """

        url = reverse('wishlist-detail', kwargs={'wishlist_id': self.wishlist.id})  # Adjust URL name and kwargs key
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("response.data",response.data)
        self.assertEqual(UUID(response.data['data']['id']), self.wishlist.id)  # Ensure the correct wishlist is retrieved

    def test_update_wishlist_success(self):
        """
        Ensure we can update a wishlist.
        """

        url = reverse('wishlist-detail', kwargs={'wishlist_id': self.wishlist.id})  # Adjust URL name and kwargs key
        update_data = {'name': 'Updated Wishlist'}  # Adjust fields to those your model and serializer support
        response = self.client.put(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.wishlist.refresh_from_db()
        self.assertEqual(self.wishlist.name, 'Updated Wishlist')  # Adjust field names accordingly

    def test_delete_wishlist_success(self):
        """
        Ensure we can delete a wishlist.
        """

        url = reverse('wishlist-detail', kwargs={'wishlist_id': self.wishlist.id})  # Adjust URL name and kwargs key
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Wishlist.DoesNotExist):
            Wishlist.objects.get(id=self.wishlist.id)

    # Add more tests here for invalid scenarios and future authentication checks

    def tearDown(self):
        pass  # Cleanup after each test if necessary
