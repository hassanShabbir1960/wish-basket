
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from wishlist.models import Wishlist
from wishlist.serializers import WishlistSerializer
from django.core.exceptions import ObjectDoesNotExist
class WishlistAPI(APIView):
    def post(self, request, *args, **kwargs):
        # Passing request data to serializer to validate
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
            ## Input data will only be valid, if :
            ## 1) Products IDs given actually exist
            ## 2) User ID given exists
            ## 3) Products array is not empty
            serializer.save()
            return Response( {"data":serializer.data,
                              "message":"Wish list successfully created",
                              "success": True
                              },
                               status=status.HTTP_201_CREATED
                              )

        return Response({"error": serializer.errors,
                         "success": False
                         },
                        status=status.HTTP_400_BAD_REQUEST
                        )

    def get(self, request, *args, **kwargs):
        wishlist_id = kwargs.get('wishlist_id')
        if wishlist_id:
            try:
                wishlist = Wishlist.objects.get(id=wishlist_id)
            except ObjectDoesNotExist:
                return Response({"error": "Wishlist does not exist",
                                 "success": False
                                 },
                                status=status.HTTP_404_NOT_FOUND
                                )

            return Response({"data":WishlistSerializer(wishlist, many=False).data,
                             "success":True},
                            status=status.HTTP_200_OK)

        # Fetch all Wishlist objects from the database
        wishlists = Wishlist.objects.all()
        if not wishlists: ## Checking if list is not empty
            return Response({"message":"No wishlists in db"},status=status.HTTP_204_NO_CONTENT)

        # Serialize the wishlists using the WishlistSerializer
        serializer = WishlistSerializer(wishlists,many=True)  ## Keeping many=True, because serializing/querying multiple Wishlist objects, not just a single instance.
        # Return a Response with the serialized data
        return Response(serializer.data,status=200)

    def put(self, request, *args, **kwargs):
        wishlist_id = kwargs.get('wishlist_id')
        if wishlist_id:
            try:
                wishlist = Wishlist.objects.get(id=wishlist_id)
            except ObjectDoesNotExist:
                return Response({"error": "Wishlist with this id does not exist",
                                 "success": False
                                 },
                                status=status.HTTP_404_NOT_FOUND
                                )

            serializer = WishlistSerializer(wishlist, data=request.data, partial=True)  # assuming partial update
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data,
                                 "message":f'Successfully updated wishlist id {wishlist_id}',
                                 "success":True},
                                  status=status.HTTP_200_OK
                                )
            return Response({"error":serializer.errors,
                             "message":"Cannot serialize this object",
                             "success":False}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({
                "error": "Please Provide id",
                "success": False},
                status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        wishlist_id = (kwargs.get('wishlist_id'))
        if wishlist_id:
            try:
                wishlist = Wishlist.objects.get(id=wishlist_id)
            except ObjectDoesNotExist:
                return Response({"error": "Wishlist does not exist",
                                 "success": False
                                 },
                                status=status.HTTP_404_NOT_FOUND
                                )
            wishlist.delete()
            return Response({"message": "Wishlist has been deleted.",
                             "success":True},
                             status=status.HTTP_204_NO_CONTENT)

