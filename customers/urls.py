from django.urls import path
from . import views
from .views import contact_form_submission
from django.shortcuts import render

urlpatterns = [
    path('account/', views.account, name='account'),
    path('contact/', contact_form_submission, name='contact_form_submission'),
    path('success/', lambda request: render(request, 'success.html'), name='success'),


]