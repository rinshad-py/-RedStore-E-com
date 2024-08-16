from django import template

register = template.Library()

@register.simple_tag(name="total")

def total(cart):
    subtotal = 0
    for item in cart.added_items.all():
        subtotal += item.product.price * item.quantity

    tax = 0.05 * subtotal
    total = tax + subtotal
    round_price = round(total)
    return round_price

