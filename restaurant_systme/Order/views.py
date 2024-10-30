from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def display_Order(request):
    return render(request, 'Order/OrderDisplay.html')