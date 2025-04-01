from django.shortcuts import render,get_object_or_404
from .models import  Category,Product,ProductCharacteristic,ProductImage
import unidecode
# Create your views here.
def products_list(request):

    category_tree = get_category_tree()
    context={
     'category_tree': category_tree
     
    }
    return render(request,'products/home.html',context)

def category_detail(request,category_choice):
    category = get_object_or_404(Category,slug=category_choice)
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

def product_category(request, category_choice):
    category = get_object_or_404(Category, slug=category_choice)
    subcategories = category.get_subcategories()
    category_tree = get_category_tree() 
    products = Product.objects.filter(category__in=[category] + list(subcategories))
    #characteristics = ProductCharacteristic.objects.filter(product=product

    context = {
        'category': category,
        'category_tree': category_tree,
        'products': products,
        #'characteristics': characteristics,
       
    }

    return render(request, 'products/products_category.html', context=context)

def product_details_main(request,slug):
    product=get_object_or_404(Product,slug=slug)
    images=ProductImage.objects.filter(product=product)
    characteristics = ProductCharacteristic.objects.filter(product=product)
    category_tree = get_category_tree()
    context = {
        'category_tree': category_tree,
        'product': product,
        'characteristics': characteristics,
        'images':images
    } 
    return render(request, 'products/product_details_main.html',context=context)


def product_details_characteristic(request,slug):
    product=get_object_or_404(Product,slug=slug)
    category_tree = get_category_tree()
    characteristics = ProductCharacteristic.objects.filter(product=product)
    context = {
        'category_tree': category_tree,
        'product': product,
        'characteristics': characteristics,
    } 
    return render(request, 'products/product_details_characteristic.html',context=context)

def product_details_reviews(request,slug):
    product=get_object_or_404(Product,slug=slug)
    category_tree = get_category_tree()
    context = {
        'category_tree': category_tree,
        'product': product,
    } 
    return render(request, 'products/product_details_reviews.html',context=context)


