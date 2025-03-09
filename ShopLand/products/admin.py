from django.contrib import admin
from .models import Category, Product,Characteristic, ProductCharacteristic
from django.utils.html import format_html
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('parent','created_at', 'updated_at')

class ProductCharacteristicInline(admin.TabularInline):
    model = ProductCharacteristic
    extra = 1  
    fields = ('characteristic', 'value')  
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available', 'created_at', 'updated_at')
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'price', 'available', 'created_at', 'updated_at')
    inlines = [ProductCharacteristicInline] 
    
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['category'].queryset = Category.objects.exclude(parent__isnull=True)
        return form


@admin.register(Characteristic)
class CarecteristicAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at', 'updated_at')
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'created_at', 'updated_at')
   
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['category'].queryset = Category.objects.exclude(parent__isnull=True)
        return form
