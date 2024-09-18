from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Reservation, Table, MenuItem
from .forms import ReservationForm

def home(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'home.html', {'menu_items': menu_items})

def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            try:
                reservation = form.save(commit=False)
                reservation.user = request.user
                reservation.save()
                messages.success(request, "Reservation created successfully!")
                return redirect('home')
            except ValueError as e:
                form.add_error(None, e)
    else:
        form = ReservationForm()
    return render(request, 'reservation_form.html', {'form': form})

def my_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'my_reservations.html', {'reservations': reservations})

def cancel_reservation(request, pk):
    reservation = Reservation.objects.get(pk=pk, user=request.user)
    if reservation:
        reservation.delete()
        messages.success(request, "Reservation canceled.")
    return redirect('my_reservations')




# Create your views here.
