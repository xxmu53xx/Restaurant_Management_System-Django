from django.shortcuts import render
from django.http import JsonResponse
from .models import User

from django.http import Http404, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')

def display_user(request):
    users = User.objects.all()
    return render(request, 'User/UserDisplay.html', {'users': users})

def add_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({'success': False, 'message': 'Username already exists.'})
        
        user = User(username=username, password=password, role=role)
        user.save()
        return JsonResponse({'success': True, 'message': 'User added successfully.', 'user': {
            'username': user.username, 'password': user.password, 'role': user.role}})
    return JsonResponse({'success': False, 'message': 'Invalid request.'})
@login_required(login_url='login')
@require_http_methods(["GET"])
def get_user(request, id):
    try:
        user = get_object_or_404(User, id=id)
        data = {
            'id': user.id,
            'username': user.username,
            'role': user.role if hasattr(user, 'role') else None,  # Adjust based on your user model
        }
        return JsonResponse(data)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@login_required(login_url='login')
@require_http_methods(["POST"])
def update_user(request, id):
    try:
        user = get_object_or_404(User, id=id)

        # Get new data from request
        new_username = request.POST.get('username')
        new_password = request.POST.get('password')
        new_role = request.POST.get('role')  # Assuming you have a role field

        # Validate username
        if User.objects.filter(username=new_username).exclude(id=id).exists():
            return JsonResponse({'success': False, 'message': 'Username already exists.'}, status=400)

        # Update user details
        user.username = new_username
        user.password = new_password  # Make sure to hash the password before saving
        user.role = new_role
        user.save()

        return JsonResponse({
            'success': True,
            'message': 'User updated successfully.',
            'user': {
                'username': user.username,
                'role': user.role,
            }
        })
    except User.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'User not found.'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=500)

@login_required(login_url='login')
@require_http_methods(["DELETE"])
def delete_user(request, id):
    try:
        user = get_object_or_404(User, id=id)
        user.delete()
        return JsonResponse({
            'success': True,
            'message': 'User deleted successfully!'
        })
    except User.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'User not found.'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=500)