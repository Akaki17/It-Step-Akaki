from django.urls import path
from . import views

app_name = 'book_orders'

urlpatterns = [
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/add/<int:pk>/', views.add_cart_item, name='add_cart_item'),
    path('cart_update/<int:pk>/', views.update_cart_item, name='update_cart_item'),
    path('cart/delete/<int:pk>/', views.delete_cart_item, name='delete_cart_item'),
    path('order/<int:pk>/', views.order_detail_view, name='order_detail'),
    path('orders/', views.list_orders_view, name='orders'),
]
