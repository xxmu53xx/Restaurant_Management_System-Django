from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout  
from django.http import HttpResponseRedirect

def redirect_login(request):
    return HttpResponseRedirect('/login/')

# Login function
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            # Check the user's permissions
            if user.is_superuser and user.is_staff:
                return redirect('dashboard_view')  # Redirect to admin dashboard
            else:
                return redirect('cashier_home_view')  # Redirect to cashier home view
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, 'accounts/login.html')

# logout function
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

# signup function
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        role = request.POST['role']

        # Validate passwords
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')

        # Check for duplicate username or email
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('signup')

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        # Set user privileges based on role
        if role == 'Admin':
            user.is_staff = True
            user.is_superuser = True
        else:
            user.is_staff = False
            user.is_superuser = False

        user.save()

        # Success message and redirect
        messages.success(request, 'Account created successfully')
        return redirect('login')

    return render(request, 'accounts/signup.html')

# reset password function
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

# forgot password function
def forgot_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            return redirect('reset_password', username=user.username)   
        except User.DoesNotExist:
            messages.error(request, 'Username not found')
    return render(request, 'accounts/forgot_password.html')

# home / dashboard function
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')
