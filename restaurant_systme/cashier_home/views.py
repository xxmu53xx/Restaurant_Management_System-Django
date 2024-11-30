from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from accountsAdmin.Menu.models import Menu

@login_required(login_url='login')
def cashier_home_view(request):
    menus = Menu.objects.all()
    return render(request, 'cashier_home.html',  {'menus': menus}) 