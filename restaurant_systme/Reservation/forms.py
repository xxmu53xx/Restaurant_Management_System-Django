# forms.py
from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['reservation_id', 'reservation_date', 'number_of_people']
        widgets = {
            'reservation_date': forms.DateInput(attrs={'type': 'date'}),
            'number_of_people': forms.NumberInput(),
        }
