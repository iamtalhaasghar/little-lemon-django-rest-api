from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from .models import MenuItem
from django.views.decorators.csrf import csrf_exempt
from django.forms import model_to_dict
from .serializers import MenuItemSerializer
from rest_framework import generics

# Create your views here.

@csrf_exempt
def menu_items(request):
    if request.method == 'GET':
        books = MenuItem.objects.all().values()
        return JsonResponse({'books': list(books)})
    elif request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        menu_item = MenuItem(name=name, price=price)
        menu_item.save()
        return JsonResponse(model_to_dict(menu_item))


class MenuItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


     
