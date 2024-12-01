from django.http import JsonResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from cashier_home.models import Payment

@login_required(login_url='login')
def payment_view(request):
    payments = Payment.objects.all().order_by('-payment_date')  # Fetch all payments to display
    return render(request, 'Payment/Payment.html', {'payments': payments})

@login_required(login_url='login')
@require_http_methods(["POST"])
def update_payment(request, payment_id):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        payment_method = request.POST.get('payment_method')

        # Validate the payment method
        if payment_method not in dict(Payment.PAYMENT_METHOD_CHOICES):
            return JsonResponse({'message': 'Invalid payment method'}, status=400)

        try:
            payment = Payment.objects.get(payment_id=payment_id)
            payment.customer_name = customer_name
            payment.payment_method = payment_method
            payment.payment_date = timezone.now()  # Update the payment date to current time
            payment.save()

            return JsonResponse({'message': 'Payment updated successfully'})
        except Payment.DoesNotExist:
            return JsonResponse({'message': 'Payment not found'}, status=404)

@login_required(login_url='login')
@require_http_methods(["DELETE"])
def delete_payment(request, payment_id):
    try:
        payment = get_object_or_404(Payment, payment_id=payment_id)
        payment.delete()
        return JsonResponse({
            'success': True,
            'message': 'a reservation list deleted successfully!'
        })
    except Payment.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'reservation not found.'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=500)