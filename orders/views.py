from django.shortcuts import render, redirect
from .models import Order, OrderedItem
from products.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def cart(request):
    user = request.user
    customer = user.customer_profile
    cart_obj, created = Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE
    )
    context = {'cart': cart_obj}
    return render(request, 'cart.html', context)

def remove_item_from_cart(request, pk):
    item = OrderedItem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')

def checkout_cart(request):
    if request.method == 'POST':
        try:
            user = request.user
            customer = user.customer_profile
            total = float(request.POST.get("total"))
            
            order_obj= Order.objects.get(
                owner=customer,
                order_status=Order.CART_STAGE
            )
            if order_obj:
                order_obj.order_status = Order.ORDER_CONFIRMED
                order_obj.total_price = total
                order_obj.save()
                status_message = "Your Order is processed. Your item delivery in 2 days"
                messages.success(request, status_message)
            else:
                status_message = "Unable to processed."
                messages.error(request, status_message)

        except Exception as e:
            status_message = "Unable to processed."
            messages.error(request, status_message)

    return redirect("cart")     


@login_required(login_url='account')
def add_to_cart(request):
    if request.method == 'POST':
        user = request.user
        customer = user.customer_profile
        quantity = int(request.POST.get("quantity"))
        product_id = request.POST.get("product_id")
        
        cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        
        # Retrieve or create an OrderedItem
        product = Product.objects.get(pk=product_id)
        ordered_item, item_created = OrderedItem.objects.get_or_create(
            product=product,
            owner=cart_obj
        )
        
        # Update the quantity and price
        ordered_item.quantity += quantity
        ordered_item.price = product.price * ordered_item.quantity
        ordered_item.save()

        messages.success(request, 'Item added to cart!')

        return redirect('list_product')
    

@login_required(login_url='account')
def view_orders(request):
    user = request.user
    customer = user.customer_profile
    all_orders = Order.objects.filter(owner=customer).exclude(order_status = Order.CART_STAGE)
    context = { 'orders': all_orders }

    return render(request, 'order.html', context)













