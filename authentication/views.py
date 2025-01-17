from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# ALL MODELS #
from .models import Customers
from django.contrib.auth.models import User

# Python modules
import hashlib

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if email not in User.objects.values_list('email',flat=True):
            print(email not in User.objects.values_list('email',flat=True))
            print(email not in User.objects.values_list('email',flat=True))
            if pass1 == pass2:
                # Save to User model
                user = User.objects.create_user(username=email,email=email,password=pass2)
                user.first_name = fname
                user.last_name = lname
                user.save()
                # Save to Customer model
                password = hashlib.md5(pass2.encode('utf-8')).hexdigest()
                Customers.objects.create(fname=fname,lname=lname,email=email,phone=phone,password=password)
                
                messages.success(request,"Account created! Please login and use the code from your email to verify your account.")
                
                return render(request, 'register.html',{'result':'success'})
            else:
                messages.error(request,"The passwords do not match!")
                
                return render(request, 'register.html', {'result':'warning'})
        else:
            messages.error(request,"An account with this E-mail already exist!")
                
            return render(request, 'register.html',{'result':'warning'})
                
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request,"Invalid credentials! Please try again.")
            
            return render(request, 'login.html',{'result':'danger'})
    return render(request, 'login.html',{})

def account_view(request):
    if request.user.is_authenticated:
        
        return render(request, 'account.html', {})

def logout_view(request):
    logout(request)
    return redirect('home')