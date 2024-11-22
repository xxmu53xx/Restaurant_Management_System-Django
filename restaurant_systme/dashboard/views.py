from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here
@login_required(login_url='login')  # Redirect to the 'login' URL if not authenticated
def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html' , {'user': request.user})

def redirect_employeeSchedule(request):
    return redirect('employeeSchedule') 

def redirect_User(request):
    return redirect('User')

'''
def redirect_Order(request):
    return redirect('displayOrder')

def redirect_Reservation(request):
    return redirect('displayReservation')

def redirect_Payment(request):
    return redirect('displayPayment')

def redirect_Menu(request):
    return redirect('displayMenu')
'''