from django.contrib import admin
from User.models import User
# Register your models here.
class ScheduleAdmin(admin.ModelAdmin):
    ordering = ['employee_id'] 
    
# Admin account: cobaa pass: 123
admin.site.register(User) 