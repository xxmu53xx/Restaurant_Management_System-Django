from django.shortcuts import render

# Create your views here.

def display_Payment(request):
    return render(request, 'Payment/PaymentDisplay.html')