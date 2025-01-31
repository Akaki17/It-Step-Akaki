from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import ProductForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
import logging

from django.views.generic import TemplateView, DetailView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



logger = logging.getLogger(__name__)  
# Create your views here.
def index(request):
    product_name = request.GET.get('product_name')
    category = request.GET.getlist('category')

    if product_name:
        products = Product.objects.filter(name__icontains=product_name)
    elif category:
        products = Product.objects.filter(category__in=category)
    else:
        products = Product.objects.all().order_by('name')  # Order by 'name' or any other field

    paginator = Paginator(products, 8)

    try:
        page_number = request.GET.get('page')
        logger.info(f'Page: {page_number}')
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
        logger.error(f'User tried to open not integer page')
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
        logger.error(f'Page Not Found, Redirecting to {paginator.num_pages}')

    categories = Category.objects.all()
    category_by_type = {}

    for category in categories:
        category_type = category.category_type
        if category_type not in category_by_type:
            category_by_type[category_type] = []
        category_by_type[category_type].append(category)

    cart_item_count = request.session.get('cart_item_count', 0)
    return render(request, 'index.html', {
        'products': products,
        'categories_by_type': category_by_type,
        'cart_item_count': cart_item_count
    })


class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get(self, request, *args, **kwargs):
            product_name = request.GET.get('product_name')
            category = request.GET.getlist('category')
        
            if product_name:
                products = Product.objects.filter(name__icontains=product_name)
            elif category:
                products = Product.objects.filter(category__in=category)
            else:
                products = Product.objects.all()
                

            paginator = Paginator(products, 8)

            try:        
                page_number = request.GET.get('page')
                logger.info(f'Page: {page_number}')  
                products = paginator.page(page_number)
            except PageNotAnInteger:
                products = paginator.page(1)
                logger.error(f'User tried to open not integer page')  
            except EmptyPage:
                products = paginator.page(paginator.num_pages)
                logger.error(f'Page Not Found, Redirecting to {paginator.num_pages}')  
            
            categories = Category.objects.all()
            category_by_type = {}
            
            for category in categories:
                category_type = category.category_type
                if category_type not in category_by_type:
                    category_by_type[category_type] = []
                category_by_type[category_type].append(category)
            
            cart_item_count = request.session.get('cart_item_count', 0)
            return render(request, self.template_name, {
                'products': products,
                'category_by_type': category_by_type,
                'cart_item_count': cart_item_count,
            })
            print(category_by_type)
            
            return render(request, self.template_name, {'products': products, 'categories_by_type': category_by_type})




@login_required(login_url='/users/login/')
def detail_product(request, pk):
    product = Product.objects.get(pk=pk)
    related_products = Product.objects.filter(category__in=product.category.all()).exclude(id=product.id)[:4]
    return render(request, 'detail_product.html', {'product': product, 'related_products': related_products})
    
    
class ProductDetailView(DetailView):
    template_name = 'detail_product.html'
    context_object_name = 'product'
    model = Product 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        related_products = Product.objects.filter(category__in=product.category.all()).exclude(id=product.id)[:4]
        print(f'Context Before related_products: {context}')
        context['related_products'] = related_products
        print(f'Context After related_products: {context}')
        return context 


    
def add_product(request):
    if request.user.has_perm('shope.add_product'):  
        if request.method == 'POST':
            form = ProductForm(request.POST,request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                product.save()
                form.save_m2m()
                return redirect('shope:index')
        else:
            form = ProductForm()
            return render(request, 'add_product.html', {'form': form})
    else:
        return redirect('shope:index') 
#

class AddProductView(FormView):
    form_class = ProductForm
    template_name = 'Add_Product.html'
    success_url = reverse_lazy('shope:index-cbv')
    def form_valid(self, form):
        product = form.save(commit=False)
        product.save()
        form.save_m2m()
        return super().form_valid(form)
    def form_invalid(self, form):
        return super().form_invalid(form)