from django.urls import path
from . import views

urlpatterns = [
    # accountsAdmin dashboard url
    path('',views.dashboard_view, name='dashboard_view')
]
