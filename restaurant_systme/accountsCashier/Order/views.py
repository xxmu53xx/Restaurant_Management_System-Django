import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from cashier_home.models import Order


@login_required(login_url='login')
def order_view(request):
    orders = Order.objects.all().order_by('-order_date')
    return render(request, 'Order/Order.html', {'orders': orders})

# Update Order
@login_required(login_url='login')
@require_http_methods(["POST"])
def update_order(request, order_id):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        total_items = request.POST.get('total_items')
        total_amount = request.POST.get('total_amount')

        try:
            order = Order.objects.get(order_id=order_id)
            order.customer_name = customer_name
            order.total_items = total_items
            order.total_amount = total_amount
            order.save()

            return JsonResponse({'message': 'Order updated successfully'})
        except Order.DoesNotExist:
            return JsonResponse({'message': 'Order not found'}, status=404)

# Delete Order
@login_required(login_url='login')
@require_http_methods(["DELETE"])
def delete_order(request, order_id):
    if request.method == 'DELETE':
        try:
            order = Order.objects.get(order_id=order_id)
            order.delete()

            return JsonResponse({'message': 'Order deleted successfully'})
        except Order.DoesNotExist:
            return JsonResponse({'message': 'Order not found'}, status=404)