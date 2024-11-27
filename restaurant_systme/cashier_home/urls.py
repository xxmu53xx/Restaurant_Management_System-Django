from django.urls import path
from . import views

urlpatterns = [
    path('', views.cashier_home_view, name='cashier_home_view'),
]