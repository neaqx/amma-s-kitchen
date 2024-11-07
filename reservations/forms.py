from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['guests', 'table', 'date', 'time']
        widgets = {
            'guests': forms.NumberInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Number of Guests'
                }
            ),
            'table': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'time': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'}
            ),
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Username'}
            ),
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Email'}
            ),
            'password1': forms.PasswordInput(
                attrs={'class': 'form-control', 'placeholder': 'Password'}
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Confirm Password'
                }
            ),
        }