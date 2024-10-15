from django.urls import path
from . import views

urlpatterns = [
    path('success/',views.success_viewer,name='successdashboard'),
]
