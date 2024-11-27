from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from accountsAdmin.employeeSchedule.models import EmSchedule
from accountsAdmin.employeeSchedule.forms import ScheduleForm

@login_required(login_url='login')
@require_http_methods(["GET"])
def employeeSchedule_view(request):
    schedules = EmSchedule.objects.all().order_by('employee_id')
    return render(request, 'employeeSchedule/employeeSchedule.html', {'schedules': schedules})

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
    return render(request, 'employeeSchedule/add_schedule.html', {'form': form})

@login_required(login_url='login')
@require_http_methods(["GET"])
def get_schedule(request, schedule_id):
    schedule = get_object_or_404(EmSchedule, schedule_id=schedule_id)
    return JsonResponse({
        'employee_id': schedule.employee_id,
        'employee_role': schedule.employee_role,
        'shift_date': schedule.shift_date.strftime('%Y-%m-%d'),
        'shift_time': schedule.shift_time.strftime('%H:%M'),
        'end_time': schedule.end_time.strftime('%H:%M'),
    })

@login_required(login_url='login')
@require_http_methods(["POST"])
def update_schedule(request, schedule_id):
    schedule = get_object_or_404(EmSchedule, schedule_id=schedule_id)
    form = ScheduleForm(request.POST, instance=schedule)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True, 'message': 'Schedule updated successfully!'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid form data.', 'errors': form.errors.as_json()}, status=400)

@login_required(login_url='login')
@require_http_methods(["POST"])
def delete_schedule(request, schedule_id):
    schedule = get_object_or_404(EmSchedule, schedule_id=schedule_id)
    schedule.delete()
    return JsonResponse({'success': True, 'message': 'Schedule deleted successfully!'})
