from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Payment
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def display_Payment(request):
    payments = Payment.objects.all()  # Fetch all payments to display
    return render(request, 'Payment/PaymentDisplay.html', {'payments': payments})

def add_payment(request):
    if request.method == 'POST':
        payment_id = request.POST.get('payment_id')  # Get the payment_id from the form
        payment_method = request.POST.get('payment_method')
        payment_date = request.POST.get('payment_date')

        # Check if the payment_id already exists
        if Payment.objects.filter(payment_id=payment_id).exists():
            return JsonResponse({'success': False, 'message': 'Payment ID already exists.'})

        # Create and save the new payment
        payment = Payment(payment_id=payment_id, payment_method=payment_method, payment_date=payment_date)
        payment.save()

        return JsonResponse({'success': True, 'message': 'Payment added successfully!'})

    return JsonResponse({'success': False, 'message': 'Invalid request'})

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