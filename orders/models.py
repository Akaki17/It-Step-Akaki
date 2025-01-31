from django.db import models
from django.contrib.auth.models import User
from shope.models import Product, Cart  # Import Cart from shope
from decimal import Decimal

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='orders_cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders_cart_items')
    quantity = models.PositiveIntegerField(default=1)

    # Property method to calculate total based on quantity and product price
    @property
    def total(self):
        return Decimal(self.quantity * self.product.price if self.product else Decimal('0.00'))

    def __str__(self):
        return f"CartItem {self.id} in Cart {self.cart.id}"
    
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders_order')  # Add related_name
    order_address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, related_name='orders_order_address')  # Add related_name
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')])

    def __str__(self):
        return f"Order {self.id} by {self.user}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders_order_items')  # Add related_name
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders_order_items')  # Add related_name
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity = models.PositiveIntegerField(null=True)

    @property
    def amount(self):
        return Decimal(self.quantity * self.product.price if self.product else Decimal('0.00'))

    def __str__(self):
        return f"OrderItem {self.id} in Order {self.order.id}"

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders_address')  # Add related_name
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=10, default='00000')

    def __str__(self):
        return f'{self.street}, {self.city}, {self.region}, {self.postal_code}'


class ProceedToCheckout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders_proceed_to_checkout')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='orders_proceed_to_checkout')
    order_address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, related_name='orders_proceed_to_checkout_order_address')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=[('Credit Card', 'Credit Card'), ('PayPal', 'PayPal'), ('Apple Pay', 'Apple Pay')])
    payment_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')])
    payment_id = models.CharField(max_length=100, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    shipping_method = models.CharField(max_length=100, null=True)
    tracking_number = models.CharField(max_length=100, null=True)
    delivery_date = models.DateField(null=True)
    delivery_time = models.TimeField(null=True)
    delivery_note = models.TextField(null=True)
    cancellation_reason = models.CharField(max_length=200, null=True)
    cancellation_note = models.TextField(null=True)
    cancellation_date = models.DateField(null=True)
    cancellation_time = models.TimeField(null=True)
    cancellation_payment_method = models.CharField(max_length=20, choices=[('Credit Card', 'Credit Card'), ('PayPal', 'PayPal'), ('Apple Pay', 'Apple Pay')], null=True)
    cancellation_payment_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')], null=True)
    cancellation_payment_id = models.CharField(max_length=100, null=True)
    cancellation_total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    cancellation_shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), null=True)
    cancellation_tax_amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), null=True)
    cancellation_discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'), null=True)
    cancellation_shipping_method = models.CharField(max_length=100, null=True)
    cancellation_tracking_number = models.CharField(max_length=100, null=True)
    cancellation_delivery_date = models.DateField(null=True)
    cancellation_delivery_time = models.TimeField(null=True)
    cancellation_delivery_note = models.TextField(null=True)

    def __str__(self):
        return f'Checkout {self.id} by {self.user}'

    class Meta:
        verbose_name_plural = 'Checkouts'

    def save(self, *args, **kwargs):
        cart_total = self.cart.orders_cart_items.aggregate(models.Sum('total'))['total__sum'] or Decimal('0.00')
        self.total_amount = cart_total
        self.shipping_cost = Decimal('5.00')
        self.tax_amount = cart_total * Decimal('0.08')
        self.discount_amount = Decimal('0.00') if self.payment_method == 'Credit Card' else Decimal('10.00')
        super().save(*args, **kwargs)





class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    address = models.ForeignKey('Address', on_delete=models.CASCADE)

    def __str__(self):
        return f"Profile for {self.user.username}"


