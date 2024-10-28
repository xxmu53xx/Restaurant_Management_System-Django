from django.shortcuts import render
from django.http import JsonResponse
from .models import Menu
# Create your views here.


def display_Menu(request):
    menus = Menu.objects.all()  # Fetch all menu items from the database
    return render(request, 'Menu/MenuDisplay.html', {'menus': menus})

def add_menu(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')

        # Create a new Menu object and save it
        new_menu = Menu(name=name, price=price, description=description)
        new_menu.save()

        return JsonResponse({'success': True, 'message': 'Menu item added successfully.'})

    return JsonResponse({'success': False, 'message': 'Invalid request.'})


