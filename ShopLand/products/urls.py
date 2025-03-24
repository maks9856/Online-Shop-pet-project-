from django.urls import path
from . import views

urlpatterns = [
    path('',views.products_list,name='home'),
    path('<slug:category_choice>/',views.category_detail,name='category_detail'),
    path('product_list/<slug:category_choice>/',views.product_category,name='products_category'),
    path('product_details/<slug:slug>/',views.product_details_main,name='product_details_main'),
    path('product_details/<slug:slug>/characteristic',views.product_details_characteristic,name='product_details_characteristic'),
    path('product_details/<slug:slug>/reviews',views.product_details_reviews,name='product_details_reviews')
    
]
