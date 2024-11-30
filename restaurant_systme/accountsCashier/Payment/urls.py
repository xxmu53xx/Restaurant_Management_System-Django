from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_view, name='payment_view'),
    
    path('add/', views.add_payment, name='add_payment'),  # Add this line
    path('delete_payment/<int:payment_id>/',views.delete_payment,name='delete_payment')
]
