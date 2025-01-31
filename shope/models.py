from django.db import models
from django.conf import settings
from datetime import datetime

# Create your models here.
class Category(models.Model):
    CATEGORY_CHOICES = [ 
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Drink', 'Drink'),
        ('Smoothie', 'Smoothie'),
    ]
    name = models.CharField(max_length=30)
    category_type = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='Breakfast')
    
    class Meta:
        db_table = 'categories'
    
    def __str__(self):
        return f'{self.name} - {self.category_type}'

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.BooleanField(default=True)
    description = models.TextField()
    
    calories = models.IntegerField(blank=True, null=True, default=0)
    spiciness_level = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True, null=True, default=0)
    protein = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    category = models.ManyToManyField(Category)

    # created_at = models.DateTimeField(default=datetime.now)  # Define default value
    updated_at = models.DateTimeField(auto_now=True)
    picture = models.ImageField(upload_to='products/', default=None, null=True, blank=True)
    
    class Meta:
        db_table = 'products'
        
    def __str__(self):
        return f'Name: {self.name} - Price: {self.price} - Stock: {self.stock}'

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='shope_carts')  # Added related_name
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'carts'
    
    def __str__(self):
        return f"Cart {self.id} by {self.user}"
