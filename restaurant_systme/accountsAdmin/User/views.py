from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserCreateForm

@login_required(login_url='login')
def user_view(request):
    if request.method == "GET":
        users = User.objects.all()
        user_data = []
        for user in users:
            user_dict = {
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'last_login': user.last_login,
                'role': 'Admin' if user.is_superuser and user.is_staff else 'Cashier'
            }
            user_data.append(user_dict)
            
        return render(request, 'User/User.html', {"users": user_data})

@login_required(login_url='login')
@require_http_methods(["GET"])
def get_user(request, id):
    try:
        user = get_object_or_404(User, id=id)
        data = {
            'user_id': user.id,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'role': 'Admin' if user.is_superuser and user.is_staff else 'Cashier',
        }
        return JsonResponse(data)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

@login_required(login_url='login')
@require_http_methods(["POST"])
def update_user(request, id):
    try:
        user = get_object_or_404(User, id=id)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            
            return JsonResponse({
                'success': True,
                'message': 'User updated successfully.',
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'role': 'Admin' if user.is_superuser and user.is_staff else 'Cashier'
                }
            })
        else:
            return JsonResponse({'success': False, 'message': 'Invalid form data.', 'errors': form.errors}, status=400)
    except User.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'User not found.'}, status=404)

@login_required(login_url='login')
def add_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            return JsonResponse({
                'success': True,
                'message': 'User added successfully.',
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'role': 'Admin' if user.is_superuser and user.is_staff else 'Cashier'
                }
            })
        else:
            return JsonResponse({'success': False, 'message': 'Invalid form data.', 'errors': form.errors})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


@login_required(login_url='login')
@require_http_methods(["DELETE"])
def delete_user(request, id):
    try:
        user = get_object_or_404(User, id=id)
        user.delete()
        return JsonResponse({'success': True, 'message': 'User deleted successfully!'})
    except User.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'User not found.'}, status=404)
