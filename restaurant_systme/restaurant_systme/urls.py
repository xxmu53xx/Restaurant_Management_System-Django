"""
URL configuration for restaurant_systme project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # admin url
    path('admin/', admin.site.urls),
   
    # accounts url
    path('',include("accounts.urls")),

    # accountsAdmin dashboard url
    path('ad/Dashboard', include('dashboard.urls')),

    path('ad/employeeSchedule', include('accountsAdmin.employeeSchedule.urls')),
    path('ad/User', include('accountsAdmin.User.urls')),
    path('ad/Menu', include('accountsAdmin.Menu.urls')),
    #path('ad/Order', include('accountsAdmin.Order.urls')),
    #path('ad/Payment', include('accountsAdmin.Payment.urls')),
    #path('ad/Reservation', include('accountsAdmin.Reservation.urls'))
]
