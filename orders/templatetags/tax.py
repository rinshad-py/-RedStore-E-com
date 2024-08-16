from django import template

register = template.Library()

@register.simple_tag(name="tax")

def tax(cart):
    subtotal = 0
    for item in cart.added_items.all():
        subtotal += item.product.price * item.quantity

    tax = 0.05 * subtotal
    round_price = round(tax)

    return round_price



