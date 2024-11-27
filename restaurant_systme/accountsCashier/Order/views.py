from django.shortcuts import render, redirect
from django.http import JsonResponse
from accountsCashier.Order.models import Order
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def order_view(request):
    orders = Order.objects.all()
    return render(request, 'Order/Order.html', {'orders': orders})


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



@login_required(login_url='login')
@require_http_methods(["DELETE"])
def delete_order(request, order_id):
    try:
        order = get_object_or_404(Order, order_id=order_id)
        order.delete()
        return JsonResponse({
            'success': True,
            'message': 'Menu deleted successfully!'
        })
    except Order.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'Menu not found.'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=500)


