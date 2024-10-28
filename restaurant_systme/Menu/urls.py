from django.urls import path
from . import views
from .views import add_menu

urlpatterns = [
    path('',views.display_Menu,name='displayMenu'),
    path('add-menu/', add_menu, name='add_menu')
    
]