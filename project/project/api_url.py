
from django.urls import path, include

app_name='api'
urlpatterns=[
    path('',include('products.api_url',namespace='products'))
]