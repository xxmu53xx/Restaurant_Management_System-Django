from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from accountsAdmin.Menu.models import Menu
from django.views.decorators.csrf import csrf_exempt
from .models import Order, Payment

@login_required(login_url='login')
def cashier_home_view(request):
    menus = Menu.objects.all()
    return render(request, 'cashier_home.html',  {'menus': menus})

# Add Order
@login_required(login_url='login')
@csrf_exempt
def add_order(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        total_items = int(request.POST.get('total_items'))
        total_amount = float(request.POST.get('total_amount'))

        # Create a new Order instance
        order = Order.objects.create(
            customer_name=customer_name,
            total_items=total_items,
            total_amount=total_amount
        )

        return JsonResponse({'message': 'Order added successfully', 'order_id': order.order_id})
    return JsonResponse({'errors': ['Invalid request method.']}, status=400)

# Add Payment
@login_required(login_url='login')
@csrf_exempt
def add_payment(request):
    if request.method == 'POST':
        # Extract POST data
        order_id = request.POST.get('order_id')
        customer_name = request.POST.get('customer_name')
        payment_method = request.POST.get('payment_method')

        # Validate the order ID
        try:
            order = Order.objects.get(order_id=order_id)
        except Order.DoesNotExist:
            return JsonResponse({'errors': ['Order does not exist.']}, status=404)

        # Validate the payment method
        if payment_method not in dict(Payment.PAYMENT_METHOD_CHOICES):
            return JsonResponse({'errors': ['Invalid payment method.']}, status=400)

        # Create a new Payment instance
        payment = Payment.objects.create(
            order_id=order,
            customer_name=customer_name,
            payment_date=timezone.now(),  # Explicitly add the current time
            payment_method=payment_method
        )

        return JsonResponse({'message': 'Payment added successfully', 'payment_id': payment.payment_id})

    return JsonResponse({'errors': ['Invalid request method.']}, status=400)