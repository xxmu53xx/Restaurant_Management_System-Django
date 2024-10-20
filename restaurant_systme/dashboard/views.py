import os
from urllib import request
from django.shortcuts import render

from restaurant_systme import settings
from django.shortcuts import redirect

# Create your views here.

def success_viewer(request):
    return render(request, 'dashboard/success.html')

def redirect_eS(request):
       return redirect('display') 