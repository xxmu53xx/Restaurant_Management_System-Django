from django.urls import path
from accountsCashier.Order import views

urlpatterns = [
    path('',views.order_view,name="order_view"),

    path('add_order/', views.add_order, name='add_order'),
    path('delete_order/<int:order_id>',views.delete_order,name='delete_order')
]