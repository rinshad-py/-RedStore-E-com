from django import template

register = template.Library()

@register.simple_tag(name="getstatus")

def getstatus(order_status):
    order_status = order_status - 1
    status = ['Confirmed', 'Processed', 'Delivered', 'Rejected']
    
    return status[order_status]

