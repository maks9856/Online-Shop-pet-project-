from django.contrib import admin
from .models import Category, Product, Characteristic, ProductCharacteristic, ProductImage, CharacteristicValue
from django.utils.html import format_html

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('parent', 'created_at', 'updated_at')

class ProductCharacteristicInline(admin.TabularInline):
    model = ProductCharacteristic
    extra = 1
    fields = ('characteristic',)
  

@admin.register(CharacteristicValue)
class CharacteristicValueAdmin(admin.ModelAdmin):
    list_display = ('characteristic', 'value')
    search_fields = ('characteristic__name', 'value')
    list_filter = ('characteristic',)

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
      
        form.base_fields['characteristic'].queryset = Characteristic.objects.exclude(category__isnull=True)
        return form

class ProductImagesInline(admin.TabularInline):
    model = ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available', 'get_discount_price', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('category', 'price', 'available', 'created_at', 'updated_at')
    inlines = [ProductCharacteristicInline, ProductImagesInline]

    def get_discount_price(self, obj):
        return obj.get_discount_price()
    get_discount_price.short_description = 'Discount Price'

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['category'].queryset = Category.objects.exclude(parent__isnull=True)
        return form

@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)
    list_filter = ('category',)

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['category'].queryset = Category.objects.exclude(parent__isnull=True)
        return form
