from django.db import models
from django.contrib.auth.models import User

class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f"Table {self.number} (Seats {self.capacity})"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    party_size = models.IntegerField()

    def __str__(self):
        return f"Reservation for {self.user.username} on {self.date} at {self.time}"

    def save(self, *args, **kwargs):
        
        existing_reservations = Reservation.objects.filter(
            date=self.date, time=self.time, table=self.table
        )
        if existing_reservations.exists():
            raise ValueError("This table is already booked at the chosen time.")
        super().save(*args, **kwargs)

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

