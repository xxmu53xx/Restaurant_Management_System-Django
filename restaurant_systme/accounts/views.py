from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.utils.safestring import mark_safe
from django.contrib.auth.hashers import make_password
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        terms_accepted = request.POST.get('terms', False)

    
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            return redirect('successdashboard') 
        else:
             xd = mark_safe('Invalid username or password. <a href="forgot_password" style="color: red;">Forgot Password?</a>')  
             messages.error(request,xd)
    return render(request, 'accounts/login.html') 

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('signup') 

        user = User.objects.create_user(username=username, password=password)
        messages.success(request, 'Account created successfully! Please log in.')
        return redirect('login') 
    
    return render(request, 'accounts/signup.html')  

def success_view(request):
    return render(request, 'accounts/success.html')

def reset_password(request, username):
    if request.method == 'POST':
        new_password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            user.password = make_password(new_password)  # Hash the new password
            user.save()
            messages.success(request, 'Password reset successfully. You can log in now.')
            return redirect('login')  # Redirect to login page
        except User.DoesNotExist:
            messages.error(request, 'Invalid username.')

    return render(request, 'accounts/reset_password.html', {'username': username})

def forgot_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            return redirect('reset_password', username=username)  # Ensure this matches the name in urls.py
        except User.DoesNotExist:
            messages.error(request, 'Username does not exist.')
    
    return render(request, 'accounts/forgot_password.html')