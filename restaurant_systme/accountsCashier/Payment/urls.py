from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_view, name='payment_view'),
    
    path('update_payment/<int:payment_id>/', views.update_payment, name='update_payment'),
    path('delete_payment/<int:payment_id>/',views.delete_payment,name='delete_payment'),
]
