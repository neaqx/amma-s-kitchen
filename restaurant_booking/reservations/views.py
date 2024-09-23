from django.shortcuts import render, redirect
from .models import Reservation, Table
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required
from datetime import datetime

@login_required
def make_reservation(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
       
            reservation = form.save(commit=False)
            conflicting_reservations = Reservation.objects.filter(
                table=reservation.table, date=reservation.date, time=reservation.time
            )
            if conflicting_reservations.exists():
                return render(request, 'reservations/reservation_form.html', {'form': form, 'error': 'Double booking!'})
            
            reservation.user = request.user
            reservation.save()
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
    reservation = Reservation.objects.get(pk=pk)
    if reservation.user == request.user:
        reservation.delete()
    return redirect('my_reservations')






