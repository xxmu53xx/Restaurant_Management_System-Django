from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_view, name='reservation_view'),
    
    path('add_reservation/', views.add_reservation, name='add_reservation'),
    path('update_reservation/<int:reservation_id>/', views.update_reservation, name='update_reservation'),
    path('delete_reservation/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
]