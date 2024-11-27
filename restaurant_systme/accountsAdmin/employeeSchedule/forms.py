from django import forms
from .models import EmSchedule  

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = EmSchedule
        fields = ['employee_id', 'employee_role', 'shift_date', 'shift_time', 'end_time']
        widgets = {
            'employee_role': forms.Select(attrs={'class': 'form-control'})
        }