from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.
def account(request):
    return render(request, 'account.html')



def contact_form_submission(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save data to the database
        Contact.objects.create(name=name, email=email, message=message)

        return redirect('success')  # Redirect to a success page or similar

    return render(request, 'contact.html')
