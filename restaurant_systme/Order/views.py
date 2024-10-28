from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Order

# Create your views here.

def display_Order(request):
    orders = Order.objects.all()
    return render(request, 'Order/OrderDisplay.html', {'orders': orders})


def add_order(request):
    if request.method == 'POST':
        # This is where you can print or log the POST data
        print(request.POST)  # This will print the request data in the console

        # Process the form data
        order_id = request.POST.get('order_id')
        customer_name = request.POST.get('customer_name')
        order_date = request.POST.get('order_date')
        total_amount = request.POST.get('total_amount')

        # Add logic to save the order, e.g.:
        Order.objects.create(
            order_id=order_id,
            customer_name=customer_name,
            order_date=order_date,
            total_amount=total_amount
        )
        
        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)