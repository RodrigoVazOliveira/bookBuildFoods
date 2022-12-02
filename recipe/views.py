from django.shortcuts import render, get_object_or_404
from recipe.models import Recipe


def index(request):
    recipes = Recipe.objects.order_by('-date_time_created').filter(published = True)
    datas = {'recipes' : recipes }

    return render(request, 'recipes/index.html', datas)




def receita(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    data = {'recipe' : recipe}

    return render(request, 'recipes/receita.html', data)


def search(request):
    recipes = Recipe.objects.order_by('-date_time_created').filter(published=True)
    if 'search' in request.GET:
        name_recipe = request.GET['search']
        if name_recipe:
            recipes = recipes.filter(name__icontains=name_recipe)
        datas = {'recipes': recipes}
        return render(request, 'recipes/search.html', datas)

    return render(request, 'recipes/search.html')