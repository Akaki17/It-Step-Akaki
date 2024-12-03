from django.urls import path
from . import views
from django.conf import settings
from  django.conf.urls.static import static

app_name = 'book_shope'

urlpatterns = [
    path('', views.index, name='index'),
    path('product/add/', views.add_product, name='add_product'),
    path('product/detail/<int:pk>/', views.detail_product, name='detail_product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    