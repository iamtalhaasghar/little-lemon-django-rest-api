from django.urls import path, include
from .views import *
urlpatterns = [
    path("menu-items", MenuItemsView.as_view(), name=""),
    path("menu-items/<int:pk>", SingleMenuItemView.as_view(), name=""),
    path("category", CategoriesView.as_view(), name=""),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),


]
