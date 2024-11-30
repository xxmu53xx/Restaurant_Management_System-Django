# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_view, name='reservation_view'),
    
    path('add-reservations/', views.add_reservation, name='add_reservation'),
    path('delete-reservation/<int:reservation_id>/',views.delete_reservation,name='delete_reservation')
]
