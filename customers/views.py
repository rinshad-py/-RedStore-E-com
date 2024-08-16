from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Customer,Contact  # Assuming you have a Customer model
from django.contrib.auth import authenticate, login, logout


def sign_out(request):
    logout(request)
    return redirect('home')

def account(request):
    #registering customer
    context = {'register': True}  # Default to registration form
    if request.POST and 'register' in request.POST:
        username = request.POST.get("username")
        phone = request.POST.get("mobile")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            context['register'] = False  # Switch to login form
            return redirect('account')  # Redirect back to the account page with an error message

        # Creates user account
        user = User.objects.create_user( username=username, password=password, email=email )

        # Creates customer account
        customer = Customer.objects.create(name=username, user=user, phone=phone, address=address )

        messages.success(request, 'Account created successfully.')
        context['register'] = False  # Switch to login form after successful registration
        return render(request, 'account.html', context)
    
    
    # Handle login
    elif request.POST and 'login' in request.POST:
        context['register'] = False
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("account_details")
        else:
            messages.error(request, "invalid username/pswd")


    return render(request, 'account.html', context)


@login_required
def account_details(request):
    customer = Customer.objects.get(user=request.user)
    context = {
        'user': request.user,
        'customer': customer,
    }
    return render(request, 'account_details.html', context)



def contact_form_submission(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save data to the database
        Contact.objects.create(name=name, email=email, message=message)

        return redirect('success')  # Redirect to a success page or similar

    return render(request, 'contact.html')



