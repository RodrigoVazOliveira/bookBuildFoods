import django.shortcuts
from recipe.models import Recipe
from django.contrib.auth.models import User


def index(request):
    recipes = Recipe.objects.order_by('-date_time_created').filter(published=True)
    datas = {'recipes': recipes}

    return django.shortcuts.render(request, 'recipes/index.html', datas)


def receita(request, recipe_id):
    recipe = django.shortcuts.get_object_or_404(Recipe, pk=recipe_id)
    data = {'recipe': recipe}

    return django.shortcuts.render(request, 'recipes/receita.html', data)


def create_recipe(request):
    if request.method == 'POST':
        name = request.POST['name']
        ingredients = request.POST['ingredients']
        mode_prepare = request.POST['mode_prepare']
        time_prepare = request.POST['time_prepare']
        income = request.POST['income']
        category = request.POST['category']
        photo = request.FILES['photo']
        user = django.shortcuts.get_object_or_404(User, pk=request.user.id)
        recipe = Recipe.objects.create(name=name,
                                       ingredients=ingredients,
                                       mode_prepare=mode_prepare,
                                       time_prepare=time_prepare,
                                       income=income,
                                       category=category,
                                       people=user,
                                       photo=photo)
        recipe.save()
        return django.shortcuts.redirect('dashboard')

    return django.shortcuts.render(request, 'recipes/create_recipe.html')


def delete_recipe(request, recipe_id):
    recipe = django.shortcuts.get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    return django.shortcuts.redirect('dashboard')


def update_recipe(request, recipe_id):
    recipe = django.shortcuts.get_object_or_404(Recipe, pk=recipe_id)
    data = {
        'recipe': recipe
    }
    return django.shortcuts.render(request, 'recipes/update_recipe.html', data)


def confirm_update_recipe(request):
    if request.method == 'POST':
        recipe_id = request.POST['recipe_id']
        recipe = Recipe.objects.get(pk=recipe_id)
        recipe.name = request.POST['name']
        recipe.ingredients = request.POST['ingredients']
        recipe.mode_prepare = request.POST['mode_prepare']
        recipe.time_prepare = request.POST['time_prepare']
        recipe.income = request.POST['income']
        recipe.category = request.POST['category']

        if 'photo' in request.FILES:
            recipe.photo = request.FILES['photo']

        recipe.save()
        return django.shortcuts.redirect('dashboard')
