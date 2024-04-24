from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import *

animal = Animal.objects.create(name='Animal1', age=7)


def create_animal():
    Animal.objects.create(name='Animal2', age=8)


def index(request):
    create_animal()
    return render(request, "index.html")

# def cats(request):
#     return HttpResponse("<h2>Коты</h2>")
#
# def dogs(request):
#     return HttpResponse("<h2>Собаки</h2>")
#


def pet(request, pet_slug):
    # будем делать обращение к БД " существует ли pet_slug ?"
    if pet_slug in ['cats', 'dogs']:
        return render(request, "pet_page.html")
    return HttpResponseNotFound(f"<h2>ОШИБКА!!! Нет такой страницы!</h2><img src='https://i.pinimg.com/736x/c9/e3/eb/c9e3eb487b0deb3f50501c196e332b58.jpg'>") # будет отправлен статус код 404


def petGET(request):
    title = request.GET.get('title')# лучше примернять когда есть форма
    return HttpResponse(f"<h2>{title}</h2>")


def categories(request, categorie_id):
    return HttpResponse(f"<h2>Категории</h2><p>id:{ categorie_id }</p>")
