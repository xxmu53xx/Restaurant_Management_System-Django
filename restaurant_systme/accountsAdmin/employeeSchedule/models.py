from django.db import models

class EmSchedule(models.Model):
    schedule_id = models.AutoField(primary_key=True) 
    employee_id = models.IntegerField() 
    shift_date = models.DateField() 
    shift_time = models.TimeField() 
    end_time = models.TimeField() 

    class Meta:
        ordering = ['employee_id'] 
        
    def __str__(self):
        return f"Schedule {self.schedule_id} for Employee {self.employee_id} on {self.shift_date}"
