from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Item


myfio = "Чухвичёва Г.А."

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
    #item = next((item for item in items if item['id'] == item_id), None)
    try:
        content = {
        "item": Item.objects.get(id=item_id)
        }
        #if content is not None:
        return render(request, "item.html", content)
    except: return HttpResponseNotFound(f"item with id={item_id} not found")

def get_items(request):
    context = {
        "items": Item.objects.all()
        }
    return render(request, "items.html", context)



