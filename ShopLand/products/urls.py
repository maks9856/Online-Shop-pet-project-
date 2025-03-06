from django.urls import path
from . import views

urlpatterns = [
    path('',views.products_list,name='home'),
    path('category/<slug:slug>/',views.category_detail,name='category_detail'),
    path('product/<slug:slug>/',views.product_category,name='products_category'),
]
