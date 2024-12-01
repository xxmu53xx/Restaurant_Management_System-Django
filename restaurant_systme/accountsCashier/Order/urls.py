from django.urls import path
from accountsCashier.Order import views

urlpatterns = [
    path('',views.order_view,name="order_view"),

    path('delete_order/<int:order_id>',views.delete_order,name='delete_order'),
    path('update_order/<int:order_id>',views.update_order,name='update_order'),
]