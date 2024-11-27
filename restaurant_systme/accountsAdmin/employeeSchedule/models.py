from django.db import models

class EmSchedule(models.Model):
    ROLE_CHOICES = [
        # Back-of-house roles
        ('executive_chef', 'Executive Chef'),
        ('kitchen_manager', 'Kitchen Manager'),
        ('sous_chef', 'Sous Chef'),
        ('station_chef', 'Station Chef'),
        ('cook', 'Cook'),
        ('assistant_cook', 'Assistant Cook'),
        ('cleaning_team', 'Cleaning Team'),
        
        # Front-of-house roles
        ('head_waiter', 'Head Waiter'),
        ('receptionist', 'Receptionist'),
        ('sommelier', 'Sommelier'),
        ('bar_staff', 'Bar Staff'),
        ('waiter', 'Waiter')
    ]

    schedule_id = models.AutoField(primary_key=True) 
    employee_id = models.IntegerField() 
    # Add default value here
    employee_role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='waiter')
    shift_date = models.DateField() 
    shift_time = models.TimeField() 
    end_time = models.TimeField() 

    class Meta:
        ordering = ['employee_id'] 
        
    def __str__(self):
        return f"Schedule {self.schedule_id} for {self.get_employee_role_display()} (Employee {self.employee_id}) on {self.shift_date}"