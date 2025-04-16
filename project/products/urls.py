# filepath: g:\backend-project\venv\project\products\urls.py
from django.urls import path
from . import views

app_name = 'pro'
urlpatterns = [
    path('', views.products, name='products'),  # Use 'products' as the name
    path('<int:id>/', views.product, name='product'),  # Use 'product' as the name
    path('add-product/', views.add_product, name='add-product'),  # Use 'product' as the name
]