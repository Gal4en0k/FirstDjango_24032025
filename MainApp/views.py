from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


myfio = "Чухвичёва Г.А."

items = [
{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
{"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
{"id": 7, "name": "Картофель фри" ,"quantity":0},
{"id": 8, "name": "Кепка" ,"quantity":124},
]

def home(request):
    context = {
        "name": "Петров Петр Петрович",
        "email": "my_mail@mail.ru"
    }
    return render(request, "index.html", context)

def about(request):
    author = {
    "FirstName": "Иван",
    "SecondName": "Петрович",
    "Family": "Иванов",
    "Phone": "8-923-600-01-02",
    "email": "vasya@mail.ru"
    }
    return render(request, "about.html", {"author": author})

def get_item(request, item_id):
    # for item in items :
    #     if item['id'] == item_id:
    #         return render(request, "item.html", item)
    
    # return HttpResponseNotFound(f"item with id={item_id} not found")
    item = next((item for item in items if item['id'] == item_id), None)
    if item is not None:
        return render(request, "item.html", item)
    return HttpResponseNotFound(f"item with id={item_id} not found")

def get_items(request):
    context = {
        "items": items
    }
    return render(request, "items.html", context)



