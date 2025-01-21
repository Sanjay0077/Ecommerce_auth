
# Create your views here.
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import SellerCreationForm, CustomerRegistrationForm
from .models import *
from django.contrib.auth import authenticate, login, logout

# Admin Dashboard
@login_required
@user_passes_test(lambda user: user.user_type == 'admin')
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

# Create Seller
@login_required
@user_passes_test(lambda user: user.user_type == 'admin')
def create_seller(request):
    if request.method == 'POST':
        form = SellerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Seller account created successfully!")
            return redirect('admin_dashboard')
    else:
        form = SellerCreationForm()

    return render(request, 'create_seller.html', {'form': form})

# Customer Registration
def customer_registration(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now login.")
            return redirect('login')
    else:
        form = CustomerRegistrationForm()

    return render(request, 'customer_registration.html', {'form': form})


def home(request):
    return render(request, 'base.html')

# def loginview(request):
    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')

    #     user = User.objects.get(username=username)
    #     if user:
    #         usertype = user.user_type
    #         if usertype == 'admin':
    #             authen = authenticate(username=username,password=password)
    #             if authen is None:
    #                 messages.error(request,'Invalid credentials')
    #                 return redirect('login')
    #             else:
    #                 login(request,user)
    #                 return redirect('admin_dashboard')
    #         elif usertype == 'seller':
    #             authen = authenticate(username=username,password=password)
    #             if authen is None:
    #                 messages.error(request,'Invalid credentials')
    #                 return redirect('login')
    #             else:
    #                 login(request,user)
    #                 return redirect('create_product')
    #         elif usertype == 'customer':
    #             authen = authenticate(username=username,password=password)
    #             if authen is None:
    #                 messages.error(request,'Invalid credentials')
    #                 return redirect('login')
    #             else:
    #                 login(request,user)
    #                 return redirect('customer_page')

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

        usertype = user.user_type  # Assuming `user_type` is a field on the User model
        login(request, user)

        # Redirect based on user type
        redirects = {
            'admin': 'admin_dashboard',
            'seller': 'create_product',
            'customer': 'customer_page',
        }
        return redirect(redirects.get(usertype, 'login'))

    return render(request, 'registration/login.html')

   

def logoutview(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

@login_required
@user_passes_test(lambda user: user.user_type =='seller')
def create_product(request):
    return render(request,'create_product.html')

def customer_page(request):
    return render(request,'customer_page.html')
