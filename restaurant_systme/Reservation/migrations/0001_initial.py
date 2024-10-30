# Generated by Django 5.1.1 on 2024-10-28 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('reservation_date', models.DateField()),
                ('number_of_people', models.PositiveIntegerField()),
            ],
        ),
    ]
