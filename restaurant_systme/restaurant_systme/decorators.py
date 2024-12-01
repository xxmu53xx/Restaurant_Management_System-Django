from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            # If the user is authenticated and an admin, continue to the view
            return view_func(request, *args, **kwargs)
        else:
            # If the user is not an admin or not authenticated, redirect to the login page
            messages.error(request, "You do not have permission to access that page.")
            return redirect('login')  # Replace 'login' with your actual login URL name if it's different
        
    return _wrapped_view