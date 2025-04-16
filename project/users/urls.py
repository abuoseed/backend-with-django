from django.urls import path
from . import views

app_name = 'auther'
urlpatterns = [
    path('', views.sign ,name='sign'),
    path('login/', views.login ,name='login')
]
