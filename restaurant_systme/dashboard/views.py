from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here
@login_required(login_url='login')  # Redirect to the 'login' URL if not authenticated
def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html' , {'user': request.user})