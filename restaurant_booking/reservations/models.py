from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime 
from django.utils import timezone

class Table(models.Model):
    number = models.CharField(max_length=50)  # Tischnamen statt nur Nummern
    seats = models.IntegerField()  # Anzahl der Sitzplätze
    description = models.CharField(max_length=255, default="No description available")  # Beispiel-Default-Wert
 

    def __str__(self):
        return f"{self.number} - {self.seats} seats - {self.description}"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE )  # Es ist besser, keinen Default-Table zu setzen
    guests = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('table', 'date', 'time')  # Verhindert Doppelbuchungen

    def __str__(self):
        return f"Reservation for {self.guests} guests on {self.date} at {self.time}"


