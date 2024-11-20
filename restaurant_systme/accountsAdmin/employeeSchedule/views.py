from django.contrib import messages
from django.http import Http404, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from employeeSchedule.forms import ScheduleForm
from employeeSchedule.models import EmSchedule

@login_required(login_url='login')
@require_http_methods(["GET", "POST"])
def add_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save()
            return JsonResponse({
                'success': True,
                'message': 'Schedule added successfully!',
                'schedule_id': schedule.schedule_id
            })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Failed to add schedule.',
                'errors': form.errors.as_json()
            }, status=400)
    else:
        form = ScheduleForm()
    return render(request, 'employeeSchedule/employeeSchedule.html', {'form': form})

@login_required(login_url='login')
@require_http_methods(["GET"])
def get_schedule(request, schedule_id):
    try:
        schedule = get_object_or_404(EmSchedule, schedule_id=schedule_id)
        data = {
            'employee_id': schedule.employee_id,
            'shift_date': schedule.shift_date.strftime('%Y-%m-%d'),
            'shift_time': schedule.shift_time.strftime('%H:%M'),
            'end_time': schedule.end_time.strftime('%H:%M'),
        }
        return JsonResponse(data)
    except EmSchedule.DoesNotExist:
        return JsonResponse({'error': 'Schedule not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@login_required(login_url='login')
@require_http_methods(["POST"])
def update_schedule(request, schedule_id):
    try:
        schedule = get_object_or_404(EmSchedule, schedule_id=schedule_id)
        
        # Create a form instance with the POST data and instance
        form = ScheduleForm(request.POST, instance=schedule)
        
        if form.is_valid():
            form.save()
            return JsonResponse({
                'success': True,
                'message': 'Schedule updated successfully.'
            })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Invalid form data.',
                'errors': form.errors.as_json()
            }, status=400)

    except EmSchedule.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'Schedule not found.'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=500)

@login_required(login_url='login')
@require_http_methods(["DELETE"])
def delete_schedule(request, schedule_id):
    try:
        schedule = get_object_or_404(EmSchedule, schedule_id=schedule_id)
        schedule.delete()
        return JsonResponse({
            'success': True,
            'message': 'Schedule deleted successfully!'
        })
    except EmSchedule.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'Schedule not found.'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=500)

@login_required(login_url='login')
def display_schedule(request):
    schedules = EmSchedule.objects.all().order_by('employee_id')
    return render(request, 'employeeSchedule/eSPrint.html', {'schedules': schedules})

@login_required(login_url='login')
def display_schedulev2(request):
    schedules = EmSchedule.objects.all().order_by('employee_id')
    return render(request, 'employeeSchedule/EsDisplay.html', {'schedules': schedules})

def redirect_dashboard(request):
    return redirect('')