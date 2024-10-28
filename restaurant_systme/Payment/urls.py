from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_Payment, name='displayPayment'),
    path('add/', views.add_payment, name='add_payment'),  # Add this line
]
