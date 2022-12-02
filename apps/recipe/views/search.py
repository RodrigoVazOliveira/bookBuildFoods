import django.shortcuts
from recipe.models import Recipe


def search(request):
    recipes = Recipe.objects.order_by('-date_time_created').filter(published=True)
    if 'search' in request.GET:
        name_recipe = request.GET['search']
        if name_recipe:
            recipes = recipes.filter(name__icontains=name_recipe)
        datas = {'recipes': recipes}
        return django.shortcuts.render(request, 'recipes/search.html', datas)

    return django.shortcuts.render(request, 'recipes/search.html')
