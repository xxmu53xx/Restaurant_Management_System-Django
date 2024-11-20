from django.urls import path
from . import views
from .views import add_menu
from .views import delete_menu
urlpatterns = [
    path('display-menu/',views.display_Menu,name='displayMenu'),
    path('add-menu/', add_menu, name='add_menu'),
    path('delete_menu/<int:id>/',delete_menu,name='delete_menu'),
     path('update_menu/<int:id>/', views.update_menu, name='update_menu'), 
]