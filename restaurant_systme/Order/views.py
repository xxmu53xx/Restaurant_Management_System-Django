from django.shortcuts import render

# Create your views here.

def display_Order(request):
    return render(request, 'Order/OrderDisplay.html')