from django.shortcuts import render
from recipe.models import Recipe


def index(request):
    recipes = Recipe.objects.all()
    datas = {'recipes' : recipes }

    return render(request, 'index.html', datas)


def receita(request):
    return render(request, 'receita.html')