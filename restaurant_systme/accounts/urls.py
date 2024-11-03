from django.urls import path
from . import views
from accounts.views import login_view, logout_view, signup_view, home_view

urlpatterns = [
    path('login/', login_view, name='login'),
        path('logout/',logout_view, name='logout'),
    path('register/',views.signup_view,name='signup'),
    path('home/',views.home_view,name='HomeDashboard'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
     path('reset_password/<str:username>/', views.reset_password, name='reset_password'),

]
