from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_view, name='menu_view'),
    
    path('add_menu/', views.add_menu, name='add_menu'),
    path('delete_menu/<int:id>/', views.delete_menu, name='delete_menu'),
    path('update_menu/<int:id>/', views.update_menu, name='update_menu'),
]