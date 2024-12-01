from django.db import models
from django.utils import timezone
from datetime import datetime

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_items = models.IntegerField(default=0)  # Optional: track total number of items
    order_date = models.DateTimeField(default=timezone.now)  # Using timezone.now instead of auto_now_add
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.order_id}"

    class Meta:
        ordering = ['-order_date']  # Optional: default orderingpy

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('debit', 'Debit Card'),
        ('credit', 'Credit Card'),
        ('digital', 'Digital Wallet'),
    ]

    payment_id = models.AutoField(primary_key=True)  # Unique ID for each payment
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')  # Foreign key to Order
    customer_name = models.CharField(max_length=100)  # Name of the customer
    payment_date = models.DateTimeField(default=timezone.now)  # Using timezone.now instead of auto_now_add
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES, default='cash')  # Payment method field with choices
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"Payment {self.payment_id} - {self.customer_name} for Order {self.order_id}"

    class Meta:
        ordering = ['-payment_date']  # Optional: default ordering by payment date