from django.shortcuts import render

# Create your views here.
def display_Reservation(request):
    return render(request,'Reservation/ReservationDisplay.html')