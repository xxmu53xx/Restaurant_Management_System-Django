from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.cache import never_cache
from django.utils.safestring import mark_safe
from django.contrib.auth.hashers import make_password

from django.views.decorators.http import require_http_methods

from django.contrib.auth import logout  


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('HomeDashboard')  # Redirect to the dashboard on successful login
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']  # Get the email from form data
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('signup') 

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Account created successfully')
        return redirect('login') 
    
    return render(request, 'accounts/signup.html')

def home_view(request):
    return render(request, 'accounts/home.html')

def reset_password(request, username):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        if not new_password:
            messages.error(request, "Please enter a new password")
            return render(request, 'accounts/reset_password.html', {'username': username})

        try:
            user = User.objects.get(username=username)
            user.password = make_password(new_password)  # Hash and save the new password
            user.save()
            messages.success(request, 'Password reset successfully')
            return redirect('login')  # Redirect to login page after success
        except User.DoesNotExist:
            messages.error(request, 'Invalid username')
            return redirect('forgot_password')  # Redirect to forgot_password if username is invalid

    return render(request, 'accounts/reset_password.html', {'username': username})

def forgot_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            return redirect('reset_password', username=user.username)
        except User.DoesNotExist:
            messages.error(request, 'Username not found')
    return render(request, 'accounts/forgot_password.html')