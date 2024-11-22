from django.urls import path
from . import views

urlpatterns = [
    # accountsAdmin dashboard url
    path('',views.dashboard_view, name='dashboard'),

    # accountsAdmin urls
    path('employeeSchedule/',views.redirect_employeeSchedule,name='employeeSchedule'),
    path('User/',views.redirect_User,name='User'),

    #path('displayOrder/',views.redirect_Order,name='DisplayOrder'),
    #path('displayReservation/',views.redirect_Reservation,name='DisplayReservation'),
    #path('displayPayment/',views.redirect_Payment,name='DisplayPayment'),
    #path('displayMenu/',views.redirect_Menu,name='DisplayMenu')
]
