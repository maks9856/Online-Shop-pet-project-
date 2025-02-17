from django.shortcuts import render, get_object_or_404
from .models import Category , Products
# Create your views here.

def popular_list(request):
    products=Products.objects.filter(available=True)
    return render(request,'main/index.html',{'products':products})

def product_detail(request,slug):
    products=get_object_or_404(Products,slug=slug,available=True)
    return render (request,'main/detail.html',{'products':products})

