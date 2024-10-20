from django import forms
from .models import EmSchedule  

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = EmSchedule
        fields = ['employee_id', 'shift_date', 'shift_time', 'end_time']