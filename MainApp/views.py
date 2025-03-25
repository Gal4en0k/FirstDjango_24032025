from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


myfio = "Чухвичёва Г.А."
author = {
    "FirstName": "Иван",
    "SecondName": "Петрович",
    "Family": "Иванов",
    "Phone": "8-923-600-01-02",
    "email": "vasya@mail.ru"
}

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
    text=f""" 
    Имя: <b>{author["FirstName"]}</b><br>
    Отчество: <b> {author["SecondName"]}</b><br>
    Фамилия: <b>{author["Family"]}</b><br>
    Телефон: {author["Phone"]}<br>
    email:{author["email"]}<br>
    """
    return HttpResponse(text)

#def product(request, item_id):
#    text = ''
#    for item in items :
#        #if item['id'] == item_id:
#        for key, value in item.items():
#            if key == "id" and  value==item_id:
#                text = f""" 
#                Название: <b>{item["name"]}</b><br>
#                Количество: <b>{item["quantity"]} </b><br>
#                """  
#            break
#    if text == '':
#            text = f""" 
#               товар c id = {id} не найден
#                """
#    text = text + f"""<a href=/items> Назад к списку товаров</a><br>"""
#    return HttpResponse(text)

def get_item(request, item_id):
    for item in items :
        if item['id'] == item_id:
            result = f""" 
            <h2>Название: {item["name"]}</h2>
            <p>Количество: {item["quantity"]} </p>
            <p><a href=/items> Назад к списку товаров</a></p>
            """  
            return HttpResponse(result)
    return HttpResponseNotFound(f"item with id={item_id} not found")

#def productList(request):
#    text = ''
#    for item in items :
#         s = f"""
#            {item["id"]}. <a href=/item\{item["id"]}> {item["name"]}</a><br>
#            """
#         text = text + s 
#    return HttpResponse(text)   

def get_items(request):
    result = "<h1>Список товаров</h1><ol>"
    for item in items :
        result += f""" <li> <a href=/item/{item["id"]}> {item["name"]}</li> """
    result +="</ol>"
    return HttpResponse(result)


