from rest_framework import serializers
from book_shope.models import Product, Category

class CategorySerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Category 
        fields = ('id', 'name', 'category_type')
        
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True) # Define category field    class Meta:

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'stock', 'description', 'category', 'picture')