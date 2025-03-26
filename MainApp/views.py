from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Item
from django.core.exceptions import ObjectDoesNotExist


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
        item = Item.objects.get(id=item_id) 
        if item.colors.exists(): 
            colors = item.colors.all()  
    except ObjectDoesNotExist: 
        return HttpResponseNotFound(f"item with id={item_id} not found")
    else: 
        content = {"item": item, "colors": colors}
        return render(request, "item.html", content)

def get_items(request):
    context = {
        "items": Item.objects.all()
        }
    #return render(request, "items.html", context)
    return render(request, "item_cards.html", context)


