from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('products/', views.list_products, name='list_product'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

]