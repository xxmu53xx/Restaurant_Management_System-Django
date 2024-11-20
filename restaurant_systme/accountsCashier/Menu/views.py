
import json
from django.shortcuts import render
from django.http import Http404, HttpResponseNotAllowed, JsonResponse
from accountsCashier.Menu.models import Menu

from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
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

@login_required(login_url='login')
@require_http_methods(["DELETE"])
def delete_menu(request, id):
    try:
        menu = get_object_or_404(Menu, id=id)
        menu.delete()
        return JsonResponse({
            'success': True,
            'message': 'Menu deleted successfully!'
        })
    except Menu.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'Menu not found.'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=500)


# update here

@login_required(login_url='login')
@csrf_exempt
@require_http_methods(["PUT"])
def update_menu(request, id):
    try:
        menu_item = get_object_or_404(Menu, id=id)
        data = json.loads(request.body)  # Parse JSON data from the request body

        # Update fields if they are provided in the request data
        if 'name' in data:
            menu_item.name = data['name']
        if 'price' in data:
            menu_item.price = data['price']
        if 'description' in data:
            menu_item.description = data['description']

        menu_item.save()  # Save the updated item to the database

        return JsonResponse({
            'success': True,
            'message': 'Menu item updated successfully!',
            'menu': {
                'id': menu_item.id,
                'name': menu_item.name,
                'price': str(menu_item.price),
                'description': menu_item.description,
            }
        }, status=200)

    except Menu.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'Menu item not found.'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=500)