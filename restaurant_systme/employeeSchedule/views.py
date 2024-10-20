from django.contrib import messages
from django.shortcuts import redirect, render


from django.shortcuts import render, redirect

from employeeSchedule.forms import ScheduleForm
from employeeSchedule.models import EmSchedule 

def add_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            
            form.save()
            messages.success(request, 'Schedule added successfully!')
          
        else:
            messages.error(request, 'Failed to add schedule. Please try again.')
    else:
        
        form = ScheduleForm()
        

    return render(request, 'employeeSchedule/employeeScheduleAdd.html', {'form': form})


def display_schedule(request):
    schedules = EmSchedule.objects.all().order_by('employee_id')
    return render(request, 'employeeSchedule/eSPrint.html', {'schedules': schedules})

def display_schedulev2(request):
    schedules = EmSchedule.objects.all().order_by('employee_id')
    return render(request, 'employeeSchedule/EsDisplay.html', {'schedules': schedules})

def redirect_dashboard(request):
    return redirect('successdashboard')