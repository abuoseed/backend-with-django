

from .models import Product
from .serializer import Serializer
from rest_framework import generics

# Import or define MultipleFieldLookupMixin
# Define MultipleFieldLookupMixin directly in this file
class ProductList(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Product.objects.all()
    serializer_class = Serializer
