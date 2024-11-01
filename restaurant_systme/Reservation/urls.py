# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('reservations/', views.display_Reservation, name='displayReservation'),
    path('add-reservations/', views.add_reservation, name='add_reservation'),
    path('delete-reservation/<int:reservation_id>/',views.delete_reservation,name='delete_reservation')
]
