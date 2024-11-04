from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('base/', views.base, name='base'),
    path('navbar/', views.navbar, name='navbar'),
]
