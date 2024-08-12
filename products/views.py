from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def list_products(request):
    #returns product list page
    
    return render(request, 'products.html')

def detail_product(request):
    return render(request, 'product_detail.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')