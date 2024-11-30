from django.urls import path
from . import views

urlpatterns = [
    # accountsAdmin dashboard url
    path('',views.dashboard_view, name='dashboard_view'),

    path('update_profile/', views.update_profile, name='update_profile'),
    path('get_user_role/', views.get_user_role, name='get_user_role'),
]
