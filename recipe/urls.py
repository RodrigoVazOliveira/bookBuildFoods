from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:recipe_id>', views.receita, name='receita'),
    path('search', views.search, name='search')
]