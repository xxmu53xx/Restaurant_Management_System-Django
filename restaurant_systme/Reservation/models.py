# models.py
from django.db import models

class Reservation(models.Model):
    reservation_id = models.CharField(max_length=50, primary_key=True)
    reservation_date = models.DateField()
    number_of_people = models.PositiveIntegerField()

    def __str__(self):
        return f"Reservation {self.reservation_id} on {self.reservation_date}"



