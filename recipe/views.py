from django.shortcuts import render


def index(request):
    recipes = {
        1:'Lasanha',
        2:'Sopa de Legumes',
        3:'Sorvete',
        4:'Bolo de chocolate'
    }
    datas = {'name_recipes' : recipes }

    return render(request, 'index.html', datas)


def receita(request):
    return render(request, 'receita.html')