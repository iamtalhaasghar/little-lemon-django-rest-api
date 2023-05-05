from django.urls import path
from .views import menu_items, MenuItemListCreateAPIView
urlpatterns = [
    path("menu-items/", MenuItemListCreateAPIView.as_view(), name="")
]
