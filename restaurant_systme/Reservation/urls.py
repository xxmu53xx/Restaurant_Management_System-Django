# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('reservations/', views.display_Reservation, name='displayReservation'),
]
