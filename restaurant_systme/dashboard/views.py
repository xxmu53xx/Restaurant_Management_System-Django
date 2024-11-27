from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from accountsAdmin.Menu.models import Menu
from accountsAdmin.employeeSchedule.models import EmSchedule


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