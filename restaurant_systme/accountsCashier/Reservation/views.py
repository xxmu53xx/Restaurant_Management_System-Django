from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import Reservation
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='login')
def reservation_view(request):
    reservations = Reservation.objects.all()
    return render(request, 'Reservation/Reservation.html', {'reservations': reservations})

# Add Reservation
@require_http_methods(["POST"])
@csrf_exempt
def add_reservation(request):
    if request.method == 'POST':
        try:
            reservation = Reservation.objects.create(
                reservation_name=request.POST.get('reservation_name'),
                reservation_date=request.POST.get('reservation_date'),
                number_of_people=request.POST.get('number_of_people')
            )
            return JsonResponse({
                'status': 'success',
                'message': 'Reservation added successfully',
                'reservation_id': reservation.reservation_id
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


@login_required(login_url='login')
@require_http_methods(["POST"])
def update_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, reservation_id=reservation_id)
    
    if request.method == "POST":
        reservation_name = request.POST.get('reservation_name')
        reservation_date = request.POST.get('reservation_date')
        number_of_people = request.POST.get('number_of_people')

        # Update the reservation
        reservation.reservation_name = reservation_name
        reservation.reservation_date = reservation_date
        reservation.number_of_people = number_of_people
        reservation.save()

        return JsonResponse({"message": "Reservation updated successfully!"})

    return JsonResponse({"error": "Invalid request"}, status=400)


@login_required(login_url='login')
@require_http_methods(["POST"])
def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, reservation_id=reservation_id)
    reservation.delete()
    return JsonResponse({"message": "Reservation deleted successfully!"})