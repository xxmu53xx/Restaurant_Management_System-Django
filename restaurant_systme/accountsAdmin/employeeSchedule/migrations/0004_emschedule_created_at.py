# Generated by Django 5.1.2 on 2024-12-01 15:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeSchedule', '0003_emschedule_employee_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='emschedule',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]