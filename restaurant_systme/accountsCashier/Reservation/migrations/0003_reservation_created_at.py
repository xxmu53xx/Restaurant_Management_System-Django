# Generated by Django 5.1.2 on 2024-12-01 15:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0002_alter_reservation_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]