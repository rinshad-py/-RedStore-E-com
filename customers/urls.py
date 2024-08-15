from django.urls import path
from . import views
from .views import contact_form_submission
from django.shortcuts import render

urlpatterns = [
    path('contact/', contact_form_submission, name='contact_form_submission'),
    path('success/', lambda request: render(request, 'success.html'), name='success'),


    path('account/', views.account, name='account'),
    path('logout/', views.sign_out, name='logout'),
    path('account_details/', views.account_details, name='account_details'),

    


]