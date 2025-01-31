from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, Order, ProceedToCheckout
from shope.models import Product
from django.contrib import messages
from django.views.generic import View, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



@login_required(login_url='/users/login/')
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    # Calculate total amount and total quantity
    total_amount = sum(cart_item.total for cart_item in cart_items)
    total_quantity = sum(cart_item.quantity for cart_item in cart_items)

    # Update the cart item count in the session (for storing session data)
    request.session['cart_item_count'] = cart_items.count()

    # Debugging the cart items directly from the database
    print("DEBUG: Cart items in database:")
    for item in cart_items:
        print(f"DEBUG: Product: {item.product.name}, Quantity: {item.quantity}")

    # Return the rendered page with additional cart information
    return render(
        request,
        'cart.html',
        {
            'cart_items': cart_items,
            'total_amount': total_amount,
            'total_quantity': total_quantity,  # Add total_quantity to the context
            'cart_item_count': cart_items.count(),  # Add cart_item_count to the context
        }
    )



@login_required(login_url='/users/login/')
def add_cart_item(request, pk):
    product = get_object_or_404(Product, pk=pk)  # Ensure the product exists
    cart, created = Cart.objects.get_or_create(user=request.user)  # Get or create the cart for the user

    print(f"DEBUG: Cart for user {request.user.id} - Cart ID: {cart.id}")  # Debugging the cart

    if product.stock > 0:  # Check if the product is in stock
        # Get or create the CartItem object
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not created:
            # If the cart item already exists, increase the quantity
            print(f"DEBUG: Cart item exists for product {product.name}. Increasing quantity.")
            cart_item.quantity += 1
        else:
            # If it's a new cart item, set quantity to 1
            print(f"DEBUG: New cart item created for product {product.name}. Setting quantity to 1.")
            cart_item.quantity = 1

        cart_item.save()  # Save the cart item

        # Recalculate total amount and total quantity
        total_amount = sum(item.total for item in cart.orders_cart_items.all())
        total_quantity = sum(item.quantity for item in cart.orders_cart_items.all())

        # Debugging the updated totals
        print(f"DEBUG: Total amount: {total_amount}, Total quantity: {total_quantity}")


        response = {
            'success': True,
            'cart_item_count': cart.cartitem_set.count(),
            'total_quantity': total_quantity,
            'total_amount': total_amount
        }
        return JsonResponse(response)  
    else:
        print(f"DEBUG: Product {product.name} is out of stock.")  # Debugging if product is out of stock
        return JsonResponse({'success': False, 'message': 'Out of stock'}, status=400)  # Return error response


class AddCartItem(LoginRequiredMixin, View):
    @staticmethod
    def get(request, pk=None):
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
        
        return redirect('orders:cart_view')


@login_required(login_url='/users/login/')
def update_cart_item(request, pk):
    print("DEBUG: update_cart_item view called")  # Debugging
    if request.method == 'POST':
        print("DEBUG: POST request received in update_cart_item")  # Debugging

        # Fetch the cart item by its pk
        cart_item = get_object_or_404(CartItem, pk=pk)

        # Get the new quantity from the POST request
        new_quantity = int(request.POST.get('quantity'))  # Ensure it's an integer

        print(f"DEBUG: Submitted quantity: {new_quantity}")  # Debugging
        print(f"DEBUG: Product stock: {cart_item.product.stock}")  # Debugging stock value

        if new_quantity == 0:  # If the quantity is zero, delete the item
            cart_item.delete()
            print("DEBUG: Cart item deleted")  # Debugging
        elif new_quantity <= cart_item.product.stock:  # If the quantity doesn't exceed stock
            cart_item.quantity = new_quantity  # Update the quantity
            cart_item.save()  # Save the updated quantity
            print(f"DEBUG: Updated cart item quantity to: {cart_item.quantity}")  # Debugging
        else:
            # If the new quantity exceeds stock, show an error
            print("DEBUG: Quantity exceeds stock")  # Debugging
            messages.error(request, "Quantity exceeds stock.")

        # Get the cart associated with the cart item
        cart = cart_item.cart

        # Update the cart item count in the session
        cart_item_count = cart.orders_cart_items.count()  # Get the number of items in the cart
        request.session['cart_item_count'] = cart_item_count

        # Prepare response
        response = {
            'success': True,
            'cart_item_count': cart_item_count
        }

        # Return response based on the type of request (AJAX or regular)
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            print("DEBUG: Returning JSON response:", response)  # Debugging
            return JsonResponse(response)

        # If it's a regular request (not AJAX), redirect to the cart view
        return redirect('orders:cart_view')
    
    # Handle non-POST requests
    return redirect(request.META.get('HTTP_REFERER'))



# class UpdateCartItemView(View):
#     @staticmethod
#     def post(request, pk):
#         cart_item = get_object_or_404(CartItem, pk=pk)
#         new_quantity = int(request.POST.get('quantity'))
#         if new_quantity == 0:
#             cart_item.delete()
#         elif new_quantity <= cart_item.product.stock:
#             cart_item.quantity = new_quantity
#             cart_item.save()
#         return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/users/login/')
def delete_cart_item(request, pk):
    print("DEBUG: delete_cart_item view called")  # Debugging
    cart_item = get_object_or_404(CartItem, pk=pk)
    cart = cart_item.cart
    cart_item.delete()
    print("DEBUG: Cart item deleted")  # Debugging

    cart_item_count = cart.orders_cart_items.count()

    cart_item_count = cart.orders_cart_items.count()  # Fixed the typo here
    request.session['cart_item_count'] = cart_item_count

    response = {
        'success': True,
        'cart_item_count': cart_item_count
    }

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        print("DEBUG: Returning JSON response:", response)  # Debugging
        return JsonResponse(response)
    return redirect(request.META.get('HTTP_REFERER'))



class DeleteCartItemView(DeleteView):
    model = CartItem
    success_url = reverse_lazy('orders:cart')


@login_required(login_url='/users/login/')
def order_detail_view(request, pk):  # Added order_detail_view
    order = get_object_or_404(Order, pk=pk, user=request.user)
    order_items = order.orderitem_set.all()
    return render(request, 'order_detail.html', {'order': order, 'order_items': order_items})


@login_required(login_url='/users/login/')
def list_orders_view(request):  # Added list_orders_view
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders.html', {'orders': orders})





class ProceedToCheckoutView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            cart = Cart.objects.get(user=request.user)
            order_address = request.user.profile.address if hasattr(request.user, 'profile') else None
            total_amount = sum(item.total for item in cart.orders_cart_items.all())
            
            
            context = {
                'cart': cart,
                'order_address': order_address,
                'total_amount': total_amount,
            }

            return render(request, 'orders/checkout.html', context)
        
        except Cart.DoesNotExist:
            messages.error(request, "Your cart is empty.")
            return redirect('orders:cart_view')

    def post(self, request):
        try:
            cart = Cart.objects.get(user=request.user)
            order_address = request.user.profile.address if hasattr(request.user, 'profile') else None
            total_amount = sum(item.total for item in cart.orders_cart_items.all())

            checkout = ProceedToCheckout.objects.create(
                user=request.user,
                cart=cart,
                order_address=order_address,
                payment_method=request.POST.get('payment_method'),
                total_amount=total_amount
            )

            return redirect('orders:order_detail', pk=checkout.id)
        
        except Cart.DoesNotExist:
            messages.error(request, "Your cart is empty.")
            return redirect('orders:cart_view')
