from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation, Table
from .forms import ReservationForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.utils import timezone  # Für den Vergleich mit dem aktuellen Datum

# Startseite
def home(request):
    return render(request, 'reservations/home.html')


@login_required
def make_reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            
            if reservation.date == timezone.now().date():
                messages.error(request, 'You cannot make a reservation for today. Please select a future date.')
                return render(request, 'reservations/reservation_form.html', {'form': form})
            
           
            if reservation.guests > reservation.table.seats:
                messages.error(request, f'The selected table cannot accommodate {reservation.guests} guests. Please choose a larger table.')
                return render(request, 'reservations/reservation_form.html', {'form': form})
            
       
            conflicting_reservations = Reservation.objects.filter(
                table=reservation.table, date=reservation.date, time=reservation.time
            )
            if conflicting_reservations.exists():
                messages.error(request, 'Double booking! Please choose another time or table.')
                return render(request, 'reservations/reservation_form.html', {'form': form})
            
            reservation.user = request.user
            reservation.save()
            messages.success(request, 'Reservation successfully created!')
            return redirect('my_reservations')
    else:
        form = ReservationForm()

    return render(request, 'reservations/reservation_form.html', {'form': form})


@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations/my_reservations.html', {'reservations': reservations})


@login_required
def cancel_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    
    if reservation.user == request.user:
        reservation.delete()
        messages.success(request, 'Reservation successfully canceled!')
    else:
        messages.error(request, 'You are not authorized to cancel this reservation.')

    return redirect('my_reservations')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to Amma\'s Kitchen.')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})





