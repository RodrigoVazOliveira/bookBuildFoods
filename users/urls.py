from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('create/recipe', views.create_recipe, name='create_recipe'),
    path('delete/<int:recipe_id>', views.delete_recipe, name='delete_recipe')
]