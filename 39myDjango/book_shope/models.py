from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    category_type = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length= 30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category)
        
    def __str__(self):
        return f'Name: {self.name} - Price: {self.price} - Stock: {self.stock}'