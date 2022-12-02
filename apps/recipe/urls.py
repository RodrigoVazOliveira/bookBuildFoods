from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('<int:recipe_id>', receita, name='receita'),
    path('search', search, name='search'),
    path('create/recipe', create_recipe, name='create_recipe'),
    path('delete/<int:recipe_id>', delete_recipe, name='delete_recipe'),
    path('update/<int:recipe_id>', update_recipe, name='update_recipe'),
    path('update', confirm_update_recipe, name='send_update_recipe')
]