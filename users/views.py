from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from recipe.models import Recipe


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password2']
        if input_is_empty(name):
            messages.error(request,'O campo nome não pode ficar em branco')
            return redirect('register')

        if input_is_empty(email):
            messages.error(request,'O campo email não pode ficar em branco')
            return redirect('register')

        if passwords_not_equals(password, password_confirm):
            messages.error(request, 'As senhas não são iguais')
            return redirect('register')

        if User.objects.filter(email=email) or User.objects.filter(username=name):
            messages.error(request, 'Usuário com email {} ou username {} já existe'.format(email, name))
            return redirect('register')

        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()
        messages.success(request, 'Usuário cadastro com sucesso!')
        return redirect('login')

    return render(request, 'users/register.html')


def input_is_empty(input):
    return not input.strip()

def passwords_not_equals(password, password_confirm):
    return password != password_confirm

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if input_is_empty(email) or input_is_empty(password):
            messages.error(request, 'Email ou senha não podem ficar em branco!')
            return redirect('login')
        if User.objects.filter(email=email).exists:
            username = User.objects.filter(email=email).values()[0]['username']

            print('username: {}'.format(username))
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso!')
                return redirect('dashboard')

        return redirect('dashboard')

    return render(request, 'users/login.html')


def dashboard(request):
    if request.user.is_authenticated:
        id_user = request.user.id
        recipes = Recipe.objects.order_by('-date_time_created').filter(people=id_user)
        data = {
            'recipes' : recipes
        }
        return render(request, 'users/dashboard.html', data)
    return redirect('index')


def logout(request):
    auth.logout(request)
    return redirect('index')


def create_recipe(request):
    if request.method == 'POST':
        name = request.POST['name']
        ingredients = request.POST['ingredients']
        mode_prepare = request.POST['mode_prepare']
        time_prepare = request.POST['time_prepare']
        income = request.POST['income']
        category = request.POST['category']
        photo = request.FILES['photo']
        user = get_object_or_404(User, pk=request.user.id)
        recipe = Recipe.objects.create(name=name,
                                       ingredients=ingredients,
                                       mode_prepare=mode_prepare,
                                       time_prepare=time_prepare,
                                       income=income,
                                       category=category,
                                       people=user,
                                       photo=photo)
        recipe.save()
        return redirect('dashboard')

    return render(request, 'users/create_recipe.html')


def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    return redirect('dashboard')
