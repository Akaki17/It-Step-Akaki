from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem, Order
from book_shope.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='/users/login')
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_amount = sum(cart_item.total for cart_item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_amount': total_amount})

@login_required(login_url='/users/login')
def add_cart_item(request, pk):
    add_to_cart = True
    product = get_object_or_404(Product, pk=pk)
    
    try:
        cart, created = Cart.objects.get_or_create(user=request.user)
        if product.stock > 0:
            cart_item, cart_item_created = CartItem.objects.get_or_create(cart=cart, product=product)
            if not cart_item_created:
                cart_item.quantity += 1
            else:
                cart_item.quantity = 1
            cart_item.save()
        else: 
            add_to_cart = False
    except Exception as e:
        add_to_cart = False
        return redirect(request.META.get('HTTP_REFERER'))
    
    if add_to_cart:
        messages.success(request, f'{product.name} was added to cart.')
    else:
        messages.error(request, f'Sorry, {product.name} is out of stock')
    
    return redirect('book_orders:cart_view')

@login_required(login_url='/users/login')
def update_cart_item(request, pk):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, pk=pk)
        new_quantity = int(request.POST.get('quantity'))
        if new_quantity == 0:
            cart_item.delete()
        elif new_quantity <= cart_item.product.stock:
            cart_item.quantity = new_quantity
            cart_item.save()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/users/login')
def delete_cart_item(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk)
    cart_item.delete()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/users/login')
def order_detail_view(request, pk):  # Added order_detail_view
    order = get_object_or_404(Order, pk=pk, user=request.user)
    order_items = order.orderitem_set.all()
    return render(request, 'order_detail.html', {'order': order, 'order_items': order_items})

@login_required(login_url='/users/login')
def list_orders_view(request):  # Added list_orders_view
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders.html', {'orders': orders})
