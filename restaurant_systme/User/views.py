from django.shortcuts import render
from django.http import JsonResponse
from .forms import UserForm
from .models import User

from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')

def display_user(request):
    users = User.objects.all()
    return render(request, 'User/UserDisplay.html', {'users': users})

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # Return the newly added user's data in JSON format
            return JsonResponse({
                'success': True,
                'message': 'User added successfully!',
                'user': {
                    'username': new_user.username,
                    'password': new_user.password,  # Encrypt in production
                    'role': new_user.role
                }
            })
        else:
            return JsonResponse({'success': False, 'message': 'Invalid data provided'})
    return JsonResponse({'success': False, 'message': 'Invalid request'})