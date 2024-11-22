from django.shortcuts import redirect
from django.conf import settings
import re
from django.urls import reverse 

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Allow access to login, signup, and forgot password paths
        allowed_paths = [
            reverse('login'),
            reverse('signup'),
            reverse('forgot_password'),
        ]

        # Regex pattern for reset_password/<username>/ path
        reset_password_pattern = re.compile(r'^/reset_password/[^/]+/$')

        # Check if the user is authenticated or if the path is allowed
        if not request.user.is_authenticated and not (
            request.path in allowed_paths or reset_password_pattern.match(request.path)
        ):
            return redirect('login')

        return self.get_response(request)