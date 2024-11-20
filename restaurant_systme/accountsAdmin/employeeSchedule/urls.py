from django.urls import path
from . import views
urlpatterns = [
    
    path('Add/',views.add_schedule,name='employeeSADD'),
    path('Dddisplay/',views.display_schedule,name='employeeSDisplay'),
    path('',views.display_schedulev2,name='display'),
    path('add-schedule/', views.add_schedule, name='add_schedule'),
     path('get-schedule/<int:schedule_id>/', views.get_schedule, name='get_schedule'),
    path('delete-schedule/<int:schedule_id>/', views.delete_schedule, name='delete_schedule'),
    path('edit-schedule/',views.update_schedule,name='update_schedule'),
    path('update_schedule/<int:schedule_id>', views.update_schedule, name='update_schedule'),
   path('employeeSchedule/delete-schedule/<int:schedule_id>', views.delete_schedule, name='delete_schedule'),
]
