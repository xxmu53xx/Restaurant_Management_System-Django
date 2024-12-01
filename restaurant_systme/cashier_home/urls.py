from django.urls import path
from . import views

urlpatterns = [
    path('', views.cashier_home_view, name='cashier_home_view'),

    path('add_order/', views.add_order, name='add_order'),
    path('add_payment/', views.add_payment, name='add_payment'),
]