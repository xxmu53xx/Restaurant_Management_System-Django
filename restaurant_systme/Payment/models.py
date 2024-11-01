from django.db import models

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)  # Manual Payment ID input
    payment_method = models.CharField(max_length=100)
    payment_date = models.DateField()

    def __str__(self):
        return f"{self.payment_method} on {self.payment_date}"



