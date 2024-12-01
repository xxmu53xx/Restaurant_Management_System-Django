from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from .models import Menu
import logging
from restaurant_systme.decorators import admin_required

@admin_required
@login_required(login_url='login')
def menu_view(request):
    menus = Menu.objects.all()
    return render(request, 'Menu/Menu.html', {'menus': menus})

@login_required(login_url='login')
@csrf_exempt
def add_menu(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_menu = Menu.objects.create(
                name=data['name'],
                price=data['price'],
                description=data['description'],
                image_url=data.get('image_url'),
                status=data['status']
            )
            
            return JsonResponse({
                'success': True,
                'message': 'Menu item added successfully.',
                'menu': {
                    'id': new_menu.id,
                    'name': new_menu.name,
                    'price': str(new_menu.price),
                    'description': new_menu.description,
                    'image_url': new_menu.image_url,
                    'status': new_menu.status
                }
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Error adding menu item: {str(e)}'
            }, status=400)

    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)

logger = logging.getLogger(__name__)

@login_required(login_url='login')
@require_http_methods(["DELETE"])
def delete_menu(request, id):
    logger.info(f"Delete menu request received for id: {id}")
    try:
        menu = get_object_or_404(Menu, id=id)
        logger.info(f"Found menu item: {menu.name}")
        menu.delete()
        logger.info(f"Successfully deleted menu item: {menu.name}")
        return JsonResponse({
            'success': True,
            'message': 'Menu item deleted successfully!'
        })
    except Exception as e:
        logger.error(f"Error deleting menu item: {str(e)}")
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=500)

@login_required(login_url='login')
@csrf_exempt
@require_http_methods(["PUT"])
def update_menu(request, id):
    try:
        menu_item = get_object_or_404(Menu, id=id)
        data = json.loads(request.body)

        # Update fields if they are provided in the request data
        menu_item.name = data.get('name', menu_item.name)
        menu_item.price = data.get('price', menu_item.price)
        menu_item.description = data.get('description', menu_item.description)
        menu_item.image_url = data.get('image_url', menu_item.image_url)
        menu_item.status = data.get('status', menu_item.status)

        menu_item.save()

        return JsonResponse({
            'success': True,
            'message': 'Menu item updated successfully!',
            'menu': {
                'id': menu_item.id,
                'name': menu_item.name,
                'price': str(menu_item.price),
                'description': menu_item.description,
                'image_url': menu_item.image_url,
                'status': menu_item.status
            }
        })
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