from django.urls import path
from .views import SingleMenuItemView, MenuItemsView
urlpatterns = [
    path("menu-items/", MenuItemsView.as_view(), name=""),
    path("menu-items/<int:pk>", SingleMenuItemView.as_view(), name="")
]
