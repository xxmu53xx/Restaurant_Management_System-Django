from django.urls import path
from . import views
urlpatterns = [
    
    path('Add/',views.add_schedule,name='employeeSADD'),
    path('Dddisplay/',views.display_schedule,name='employeeSDisplay'),
    path('',views.display_schedulev2,name='display'),
    path('add-schedule/', views.add_schedule, name='add_schedule'),
]
