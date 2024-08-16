from django import template

register = template.Library()

@register.simple_tag(name="subtotal")

def subtotal(cart):
    total = 0
    for item in cart.added_items.all():
        total += item.product.price * item.quantity
    
    return total



