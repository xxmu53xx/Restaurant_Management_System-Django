from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_view, name='user_view'),
    
    path('add_user/', views.add_user, name='add_user'),
    path('update_user/<int:id>/', views.update_user, name='update_user'),
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),
    path('get_user/<int:id>/', views.get_user, name='get_user'),
]
