from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Product
from .form import Add_product
from products.models import Product
# Create your views here.


def products(request):
    return render(request, 'pages/product/products.html',{'products': Product.objects.all()})


def product(request,*args, **kwargs):
    item_product=get_object_or_404(Product,id= kwargs.get('id'))
    return render(request, 'pages/product/product.html',context={'product':item_product})


def add_product(request,*args, **kwargs):
    if request.method=='POST':
        form=Add_product(request.POST, request.FILES )
        if form.is_valid():
            form.save()
            return redirect(reverse('pro:products'))
        else:
            print(form.errors) 
            return render(request, 'pages/product/add-product.html',context={'form':form})
    
    return render(request, 'pages/product/add-product.html', {'form' : Add_product()})

