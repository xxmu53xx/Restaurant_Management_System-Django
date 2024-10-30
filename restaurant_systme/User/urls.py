from django.urls import path
from . import views
urlpatterns = [
    path('',views.display_user,name='displayUser'),
    path('add_user/', views.add_user, name='add_user')
]