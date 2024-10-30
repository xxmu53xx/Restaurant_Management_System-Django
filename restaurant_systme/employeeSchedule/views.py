from django.contrib import messages
from django.http import Http404, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect

from employeeSchedule.forms import ScheduleForm
from employeeSchedule.models import EmSchedule 

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
@require_http_methods(["GET", "POST"])
def add_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Schedule added successfully!')
            return JsonResponse({'success': True, 'message': 'Schedule added successfully!'})
        else:
            errors = form.errors.as_json()
            messages.error(request, 'Failed to add schedule. Please try again.')
            return JsonResponse({'success': False, 'message': 'Failed to add schedule.', 'errors': errors})
    else:
        form = ScheduleForm()
    
    return render(request, 'employeeSchedule/employeeSchedule.html', {'form': form})
@login_required(login_url='login')
@require_http_methods(["GET"])
def get_schedule(request, schedule_id):
    try:
        schedule = EmSchedule.objects.get(schedule_id=schedule_id)
        data = {
            'employee_id': schedule.employee_id,
            'shift_date': schedule.shift_date,
            'shift_time': schedule.shift_time,
            'end_time': schedule.end_time,
        }   
        return JsonResponse(data)
    except EmSchedule.DoesNotExist:
        return Http404("Schedule not found")
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
@login_required(login_url='login')
@csrf_exempt
def update_schedule(request, schedule_id):
    if request.method == 'POST':
        try:
            schedule = EmSchedule.objects.get(id=schedule_id)
            # Update the schedule fields
            schedule.employee_id = request.POST.get('employee_id')
            schedule.shift_date = request.POST.get('shift_date')
            schedule.shift_time = request.POST.get('shift_time')
            schedule.end_time = request.POST.get('end_time')
            schedule.save()

            return JsonResponse({'success': True, 'message': 'Schedule updated successfully.'})

        except EmSchedule.DoesNotExist: 
            return JsonResponse({'success': False, 'message': 'Schedule not found.'}, status=404)

        except Exception as e:
            print(f"Error updating schedule: {e}")
            return JsonResponse({'success': False, 'message': 'An internal server error occurred.'}, status=500)

    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)
def delete_schedule(request, schedule_id):
    if request.method == 'DELETE':
        try:
            schedule = EmSchedule.objects.get(schedule_id=schedule_id)
            schedule.delete()
            return JsonResponse({'message': 'Schedule deleted successfully!'}, status=200)
        except EmSchedule.DoesNotExist:
            return JsonResponse({'error': 'Schedule not found.'}, status=404)
    else:
        return HttpResponseNotAllowed(['DELETE'])
def display_schedule(request):
    schedules = EmSchedule.objects.all().order_by('employee_id')
    return render(request, 'employeeSchedule/eSPrint.html', {'schedules': schedules})
@login_required(login_url='login')
def display_schedulev2(request):
    schedules = EmSchedule.objects.all().order_by('employee_id')
    return render(request, 'employeeSchedule/EsDisplay.html', {'schedules': schedules})

def redirect_dashboard(request):
    return redirect('')

