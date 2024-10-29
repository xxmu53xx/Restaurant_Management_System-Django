from django.shortcuts import redirect
from django.conf import settings
from django.urls import reverse 
class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            # If not authenticated, redirect to login page unless on login or signup page
            if request.path not in [reverse('login'), reverse('signup')]:
                return redirect('login')

        # Call the next middleware or view
        response = self.get_response(request)
        return response