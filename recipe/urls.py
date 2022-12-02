from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:recipe_id>', views.receita, name='receita'),
    path('search', views.search, name='search'),
    path('create/recipe', views.create_recipe, name='create_recipe'),
    path('delete/<int:recipe_id>', views.delete_recipe, name='delete_recipe'),
    path('update/<int:recipe_id>', views.update_recipe, name='update_recipe'),
    path('update', views.confirm_update_recipe, name='send_update_recipe')
]