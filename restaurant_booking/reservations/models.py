from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Table(models.Model):
    number = models.IntegerField()
    seats = models.IntegerField()

    def __str__(self):
        return f"Table {self.number} - {self.seats} seats"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    guests = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('table', 'date', 'time')  # Prevent double bookings

    def __str__(self):
        return f"Reservation for {self.guests} guests on {self.date} at {self.time}"



