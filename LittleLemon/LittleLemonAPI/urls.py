from django.urls import path
from .views import menu_items
urlpatterns = [
    path("menu-items", menu_items, name="")
]
