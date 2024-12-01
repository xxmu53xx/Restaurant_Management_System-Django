from django.db import models
from datetime import datetime

class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    reservation_name = models.CharField(max_length=100)
    reservation_date = models.DateField()
    number_of_people = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'Reservation_reservation'

    def __str__(self):
        return f"Reservation {self.reservation_id} ({self.reservation_name}) on {self.reservation_date} for {self.number_of_people} people"