from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['guests', 'table', 'date', 'time']
        widgets = {
            'guests': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Guests'}),
            'table': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }

