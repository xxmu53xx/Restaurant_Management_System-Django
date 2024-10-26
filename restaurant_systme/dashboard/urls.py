from django.urls import path
from . import views

urlpatterns = [
    path('success/',views.success_viewer,name='successdashboard'),
    path('display/',views.redirect_eS,name='Display'),
    path('displayOrder/',views.redirect_Order,name='DisplayOrder'),
    path('displayReservation/',views.redirect_Reservation,name='DisplayReservation'),
    path('displayUser/',views.redirect_User,name='DisplayUser'),
    path('displayPayment/',views.redirect_Payment,name='DisplayPayment'),
    path('displayMenu/',views.redirect_Menu,name='DisplayMenu')
]
