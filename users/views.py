from django.shortcuts import render, redirect
from django.contrib.auth.models import User

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
    return render(request, 'users/login.html')


def dashboard(request):
    pass

def logout(request):
    pass