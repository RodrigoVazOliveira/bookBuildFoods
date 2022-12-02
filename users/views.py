from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from recipe.models import Recipe


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password2']
        validate_inputs_register(name, email, password, password_confirm)

        if User.objects.filter(email=email):
            print('Usuário com email {} já existe'.format(email))
            return redirect('register')

        user = User.objects.create_user(username=name, email=email, password=password)
        user.save()
        print('Usuário cadastro com sucesso!')

        return redirect('login')

    return render(request, 'users/register.html')


def validate_inputs_register(name, email, password, password_confirm):
    if not name.strip():
        print('O campo nome não pode ficar em branco')
        return redirect('register')

    if not email.strip():
        print('O campo email não pode ficar em branco')
        return redirect('register')

    if password != password_confirm:
        print('As senhas não são iguais')
        return redirect('register')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if email == '' or password == '':
            print('Email ou senha não podem ficar em branco!')
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
