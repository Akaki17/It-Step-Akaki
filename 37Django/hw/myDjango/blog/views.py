from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>Hello From views.py</h1>')

def main(request):
    return render(request, 'main.html')

def about(request):
    return render(request, 'about.html')

def base(request):
    return render(request, 'base.html')

def navbar(request):
    return render(request, 'navbar.html')

