from django.shortcuts import render,get_object_or_404
from .models import  Category
# Create your views here.
def products_list(request):

    category_tree = get_category_tree()
    context={
     'category_tree': category_tree
     
    }
    return render(request,'products/home.html',context)

def category_detail(request,slug):
    category = get_object_or_404(Category,slug=slug)
    category_tree = get_category_tree()
    subcategories = category.subcategories.all()
    context={
     'category': category,
     'category_tree': category_tree,
     'subcategories': subcategories
   
    }
    return render(request,'products/category_detail.html',context)

def get_category_tree(parent=None):
    categories = Category.objects.filter(parent=parent).order_by('name')
    return [
        {
            'category': category,
            'subcategories': get_category_tree(category) 
        }
        for category in categories
    ]
def product_category(request,slug):
    category=get_object_or_404(Category,slug=slug)
    category_tree = get_category_tree()
    context={
     'category': category,
     'category_tree': category_tree
    }
    return render(request,'products/products_category.html',context=context)


