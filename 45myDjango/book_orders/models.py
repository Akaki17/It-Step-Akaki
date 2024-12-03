from django.db import models
from django.contrib.auth.models import User
from book_shope.models import Product
from decimal import Decimal

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_orders_cart')  # Added related_name to avoid clashes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Cart {self.id} by {self.user}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='book_orders_cartitem')  # Added related_name to avoid clashes
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='book_orders_cartitem')  # Added related_name to avoid clashes
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total(self):
        return Decimal(self.quantity * self.product.price if self.product else Decimal('0.00'))

    def __str__(self):
        return f"CartItem {self.id} in Cart {self.cart.id}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_orders_order')  # Added related_name to avoid clashes
    order_address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, related_name='book_orders_order_address')  # Added related_name to avoid clashes
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')])

    def __str__(self):
        return f"Order {self.id} by {self.user}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name='book_orders_orderitem')  # Added related_name to avoid clashes
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='book_orders_orderitem')  # Added related_name to avoid clashes
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity = models.PositiveIntegerField(null=True)

    @property
    def amount(self):
        return Decimal(self.quantity * self.product.price if self.product else Decimal('0.00'))

    def __str__(self):
        return f"OrderItem {self.id} in Order {self.order.id}"

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book_orders_address')  # Added related_name to avoid clashes
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=10, default='00000')

    def __str__(self):
        return f'{self.street}, {self.city}, {self.region}, {self.postal_code}'
