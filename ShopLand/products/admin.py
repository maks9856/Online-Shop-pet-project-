from django.contrib import admin
from .models import Category
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','subcategory','created_at','updeted_at']
    list_filter=('name','subcategory','created_at','updeted_at')
