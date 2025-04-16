from django.urls import path
from products import api_views



app_name='products'

urlpatterns=[
    path('', api_views.ProductList.as_view(), name='items')
]