from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True, editable=False)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='subcategories'
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, editable=False)
    img = models.ImageField(upload_to='products/', blank=True)
    characteristics = models.TextField(blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'product'
        verbose_name_plural = 'products'
        indexes = [
            models.Index(fields=['id','slug']),
            models.Index(fields=['name', 'price']),
            models.Index(fields=['price']),
            models.Index(fields=['available']),
            models.Index(fields=['discount']),
            models.Index(fields=['-created_at'])
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("products:products_detail", args=[self.slug])
    
    def get_discount_price(self):
        if self.discount:
            return self.price - self.price * self.discount / 100
        return self.price
    
    
    
    
    
    

   
    
        

        
    