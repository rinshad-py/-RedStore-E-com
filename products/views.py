from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    featured_product = Product.objects.order_by('priority')[:4]
    latest_product = Product.objects.order_by('-id')[:4]

    # Add filled and empty stars to each featured product
    for product in featured_product:
        product.filled_stars = range(product.rating)
        product.empty_stars = range(5 - product.rating)

    # Add filled and empty stars to each latest product
    for product in latest_product:
        product.filled_stars = range(product.rating)
        product.empty_stars = range(5 - product.rating)
        

    context = {
        'featured_product': featured_product, 
        'latest_product': latest_product
    }

    return render(request, 'index.html', context)

def list_products(request):
    #returns product list page
    page = 1
    if request.GET:
        page = request.GET.get('page', 1)

    product_list = Product.objects.order_by('priority')
    product_paginator = Paginator(product_list, 8)
    product_list = product_paginator.get_page(page)
    context = {'products': product_list}

    # Prepare context with ratings
    for product in product_list:
        product.filled_stars = range(product.rating)
        product.empty_stars = range(5 - product.rating)

    return render(request, 'products.html', context)



def detail_product(request, pk):
    related_product = Product.objects.order_by('-id')[:4]
    # Add filled and empty stars to each featured product
    for product in related_product:
        product.filled_stars = range(product.rating)
        product.empty_stars = range(5 - product.rating)

    product = Product.objects.get(pk=pk)

    return render(request, 'product_detail.html',{'product': product, 'related_product': related_product} )


