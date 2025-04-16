from django.shortcuts import render, redirect
from django.urls import reverse
from .models import User

def sign(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    if request.method == 'POST':
        User.objects.create(email=email, password=password, name=name)
        return redirect(reverse('pro:products'))
    return render(request, 'pages/users/sign-in.html')

def login(request,*args, **kwargs):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if request.method == 'POST':
        data=User.objects.all() 
        for x in data:
            if x.email == email and x.password == password:
                return redirect(reverse('pro:products'))
                
             
            
    return render(request, 'pages/users/login-up.html')