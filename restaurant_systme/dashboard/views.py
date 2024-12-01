from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db.models import Sum

from django.contrib.auth.models import User
from cashier_home.models import Order, Payment
from accountsAdmin.employeeSchedule.models import EmSchedule
from accountsAdmin.Menu.models import Menu
from accountsCashier.Reservation.models import Reservation
from restaurant_systme.decorators import admin_required

# Create your views here
@admin_required
@login_required(login_url='login')
def dashboard_view(request):
    # Get total number of menu items
    total_menu = Menu.objects.count()

    # Get the total sum of total_items (AKA total_order in the frontend)
    total_order = Order.objects.aggregate(total_sum=Sum('total_items'))['total_sum']

    # Get the total sum of total_amount (AKA total_price in the frontend)
    total_revenue = Order.objects.aggregate(total_sum=Sum('total_amount'))['total_sum']
    total_revenue = "{:.2f}".format(total_revenue) if total_revenue is not None else "0.00"
    
    # Get total number of unique employees from schedules
    total_staff = EmSchedule.objects.values('employee_id').distinct().count()

    # Get the latest employee schedule based on created_at
    latest_schedule = EmSchedule.objects.order_by('-created_at').first()  # Fetch the most recently created schedule
    latest_user = User.objects.order_by('-last_login').first()
    latest_order = Order.objects.order_by('-order_date').first()
    latest_payment = Payment.objects.order_by('-payment_date').first()
    latest_reservation = Reservation.objects.order_by('-reservation_date').first()
    latest_menu = Menu.objects.order_by('-created_at').first()
    
    context = {
        'user': request.user,
        'total_menu': total_menu,
        'total_staff': total_staff,
        'total_order': total_order,
        'total_revenue': total_revenue,

        'latest_schedule': latest_schedule,
        'latest_user': latest_user,
        'latest_order': latest_order,
        'latest_payment': latest_payment,
        'latest_reservation': latest_reservation,
        'latest_menu': latest_menu
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