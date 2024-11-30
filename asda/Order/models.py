from django.db import models

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)


