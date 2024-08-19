from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('remove_item/<pk>', views.remove_item_from_cart, name="remove_item"),
    path('checkout/', views.checkout_cart, name='checkout'),
    
    path('view_orders/', views.view_orders, name='orders'),

]