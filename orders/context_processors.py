from .models import Cart, CartItem

def cart_info(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        cart_items = CartItem.objects.filter(cart=cart)
        
        total_amount = sum(cart_item.total for cart_item in cart_items)
        total_quantity = sum(cart_item.quantity for cart_item in cart_items)
        
        return {
            'cart_item_count': cart_items.count(),  
            'total_quantity': total_quantity,        
            'total_amount': float(total_amount),     
        }
    
    return {
        'cart_item_count': 0,
        'total_quantity': 0,
        'total_amount': 0
    }
