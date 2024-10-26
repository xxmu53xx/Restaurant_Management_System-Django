from django.shortcuts import render

# Create your views here.
def display_user(request):
    return render(request,'User/UserDisplay.html')