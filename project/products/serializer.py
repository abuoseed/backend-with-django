
from products.models import Product
from rest_framework import serializers


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'