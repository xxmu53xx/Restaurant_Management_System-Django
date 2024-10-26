from django.shortcuts import render

# Create your views here.
def display_Menu(request):
    return render(request, 'Menu/MenuDisplay.html')