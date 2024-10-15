from django.urls import path
from . import views

urlpatterns = [
   
    path('Add/',views.add_schedule,name='employeeSADD'),
    path('Display/',views.display_schedule,name='employeeSDisplay'),
]
