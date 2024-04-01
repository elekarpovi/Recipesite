from django.urls import path

from .views import *


urlpatterns = [
    path('', home, name="recipes_home"),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name="recipes_detail"),
    path('recipe/create', RecipeCreateView.as_view(), name="recipes_create"),
    path('recipe/<int:pk>/update', RecipeUpdateView.as_view(), name="recipes_update"),
    path('recipe/<int:pk>/delete', RecipeDeleteView.as_view(), name="recipes_delete"),
]