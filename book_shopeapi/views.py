from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from book_shope.models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


@api_view(['GET'])
def index(request):
    product_name = request.GET.get('product_name')
    category = request.GET.getlist('category')

    if product_name:
        products = Product.objects.filter(name__icontains=product_name)
    elif category:
        products = Product.objects.filter(category__in=category)
    else:
        products = Product.objects.all()


    paginator = PageNumberPagination()
    paginator.page_size = 8
    paginated_products = paginator.paginate_queryset(products, request)

    products_serializer = ProductSerializer(paginated_products, many=True)

    categories = Category.objects.all()
    category_by_type = {}

    for category in categories:
        category_type = category.category_type
        if category_type not in category_by_type:
            category_by_type[category_type] = []
        category_by_type[category_type].append(CategorySerializer(category).data)

    return paginator.get_paginated_response({
        'products': products_serializer.data,
        'categories_by_type': category_by_type
    })
    
@api_view(['POST'])
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        product = serializer.save()
        return Response({'message': 'Product added successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductsView(APIView):
    
    @staticmethod
    def get(request):
        product_name = request.GET.get('product_name')
        category = request.GET.getlist('category')

        if product_name:
            products = Product.objects.filter(name__icontains=product_name)
        elif category:
            products = Product.objects.filter(category__in=category)
        else:
            products = Product.objects.all()


        paginator = PageNumberPagination()
        paginator.page_size = 8
        paginated_products = paginator.paginate_queryset(products, request)

        products_serializer = ProductSerializer(paginated_products, many=True)

        categories = Category.objects.all()
        category_by_type = {}

        for category in categories:
            category_type = category.category_type
            if category_type not in category_by_type:
                category_by_type[category_type] = []
            category_by_type[category_type].append(CategorySerializer(category).data)

        return paginator.get_paginated_response({
            'products': products_serializer.data,
            'categories_by_type': category_by_type
        })
        

class AddProductView(APIView):
    @staticmethod
    def post(request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            return Response({'message': 'Product added successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
