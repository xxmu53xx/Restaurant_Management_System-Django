from django.urls import path
from . import views

urlpatterns = [
    path('', views.employeeSchedule_view, name='employeeSchedule_view'),
    
    path('add-schedule/', views.add_schedule, name='add_schedule'),
    path('get-schedule/<int:schedule_id>/', views.get_schedule, name='get_schedule'),
    path('update-schedule/<int:schedule_id>/', views.update_schedule, name='update_schedule'),
    path('delete-schedule/<int:schedule_id>/', views.delete_schedule, name='delete_schedule'),
]
