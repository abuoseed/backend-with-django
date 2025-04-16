from django import forms
from products.models import Product
class Add_product(forms.ModelForm):
    class Meta:
        fields=['name', 'description', 'image', 'active', 'price', 'category']
        model=Product
    