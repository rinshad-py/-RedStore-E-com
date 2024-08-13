from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    return render(request, 'index.html')

def list_products(request):
    #returns product list page
    page = 1
    if request.GET:
        page = request.GET.get('page', 1)

    product_list = Product.objects.all()
    product_paginator = Paginator(product_list, 4)
    product_list = product_paginator.get_page(page)
    context = {'products': product_list}

    # Prepare context with ratings
    for product in product_list:
        product.filled_stars = range(product.rating)
        product.empty_stars = range(5 - product.rating)

    return render(request, 'products.html', context)



def detail_product(request):
    return render(request, 'product_detail.html')



def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')