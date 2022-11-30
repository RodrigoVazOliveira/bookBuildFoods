from django.shortcuts import render, get_object_or_404
from recipe.models import Recipe


def index(request):
    recipes = Recipe.objects.filter(published = True)
    datas = {'recipes' : recipes }

    return render(request, 'index.html', datas)



def receita(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    data = {'recipe' : recipe}

    return render(request, 'receita.html', data)