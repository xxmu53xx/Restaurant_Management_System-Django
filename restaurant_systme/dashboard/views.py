from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accountsAdmin.Menu.models import Menu
from accountsAdmin.employeeSchedule.models import EmSchedule
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User

# Create your views here
@login_required(login_url='login')
def dashboard_view(request):
    # Get total number of menu items
    total_menu = Menu.objects.count()
    
    # Get total number of unique employees from schedules
    total_staff = EmSchedule.objects.values('employee_id').distinct().count()
    
    context = {
        'user': request.user,
        'total_menu': total_menu,
        'total_staff': total_staff
    }
    
    return render(request, 'dashboard/dashboard.html', context)

@login_required
@require_http_methods(["POST"])
def update_profile(request):
    try:
        user = request.user

        # Check if username is being changed and is unique
        if 'username' in request.POST:
            new_username = request.POST['username']
            if new_username != user.username:
                # Check if username already exists
                if User.objects.exclude(pk=user.pk).filter(username=new_username).exists():
                    return JsonResponse({
                        'success': False,
                        'message': 'Username is already taken'
                    })
                user.username = new_username

        # Update other fields
        if 'first_name' in request.POST:
            user.first_name = request.POST['first_name']
        
        if 'last_name' in request.POST:
            user.last_name = request.POST['last_name']
        
        if 'email' in request.POST:
            user.email = request.POST['email']
        
        user.save()

        return JsonResponse({
            'success': True,
            'username': user.username,
        })
    
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        })

@login_required
def get_user_role(request):
    try:
        user = request.user
        role = "Admin" if user.is_superuser or user.is_staff else "Cashier"
        return JsonResponse({'success': True, 'role': role})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})