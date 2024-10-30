from django.shortcuts import render

from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def display_Reservation(request):
    return render(request,'Reservation/ReservationDisplay.html')