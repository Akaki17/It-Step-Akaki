from django.urls import path
from . import views

app_name = 'book_shope'

urlpatterns = [
    path('', views.index, name='index'),
    path('product/add/', views.add_product, name='add_product'),
]
