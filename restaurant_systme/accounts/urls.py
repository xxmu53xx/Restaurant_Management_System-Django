from django.urls import path
from . import views

urlpatterns = [
    # accounts urls
    path('', views.redirect_login, name='redirect_login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view,name='signup'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password/<str:username>/', views.reset_password, name='reset_password'),

    # accountsAdmin dashboard url

    # accountsCashier dashboard url
    #path('home/',views.home_view,name='HomeDashboard'),

]
