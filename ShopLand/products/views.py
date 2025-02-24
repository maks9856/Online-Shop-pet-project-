from django.shortcuts import render
from .models import  Category
# Create your views here.
def products_list(request):
    data_category=Category.objects.all()
    context={
        'data_category':data_category
    }
    return render(request,'products/home.html',context)