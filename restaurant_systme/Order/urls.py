from django.urls import path
from . import views
urlpatterns = [
    path('',views.display_Order,name="displayOrder"),
    path('add_order/', views.add_order, name='add_order'),

]