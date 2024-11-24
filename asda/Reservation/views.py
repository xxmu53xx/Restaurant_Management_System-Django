from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Reservation
from .forms import ReservationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def display_Reservation(request):
    reservations = Reservation.objects.all()

    # Handle POST request (form submission)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            # Check if the request is AJAX
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                new_reservation = {
                    'reservation_id': form.instance.reservation_id,
                    'reservation_date': form.instance.reservation_date.strftime('%Y-%m-%d'),
                    'number_of_people': form.instance.number_of_people,
                }
                return JsonResponse({'success': True, 'reservation': new_reservation})
            else:
                messages.success(request, 'Reservation added successfully.')
                return redirect('displayReservation')
        else:
            # Return error response for AJAX
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'message': 'Failed to add reservation. Please check the form for errors.'})
            else:
                messages.error(request, 'Failed to add reservation. Please check the form for errors.')

    else:
        form = ReservationForm()

    # Render the template with the form and reservations
    return render(request, 'Reservation/ReservationDisplay.html', {
        'form': form,
        'reservations': reservations,
    })



@csrf_exempt
def add_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            return JsonResponse({
                'success': True,
                'reservation': {
                    'reservation_id': reservation.id,
                    'reservation_date': reservation.reservation_date,
                    'number_of_people': reservation.number_of_people
                },
                'message': 'Reservation added successfully!'
            })
        else:
            return JsonResponse({'success': False, 'message': 'Form is invalid'})
    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=400)


@login_required(login_url='login')
@require_http_methods(["DELETE"])
def delete_reservation(request, reservation_id):
    try:
        reservation = get_object_or_404(Reservation, reservation_id=reservation_id)
        reservation.delete()
        return JsonResponse({
            'success': True,
            'message': 'a reservation list deleted successfully!'
        })
    except Reservation.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'reservation not found.'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=500)