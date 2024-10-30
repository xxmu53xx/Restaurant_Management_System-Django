from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Reservation
from .forms import ReservationForm


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
            if request.is_ajax():
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
            if request.is_ajax():
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


