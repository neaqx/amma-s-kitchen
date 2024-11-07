from django.db import models
from django.contrib.auth.models import User


class Table(models.Model):
    number = models.CharField(max_length=50)
    seats = models.IntegerField()
    description = models.CharField(
        max_length=255, default="No description available"
    )

    def __str__(self):
        return f"{self.number} - {self.seats} seats - {self.description}"


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, default=1)
    guests = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('table', 'date', 'time')

    def __str__(self):
        return (
            f"Reservation for {self.guests} guests "
            f"on {self.date} at {self.time}"
        )