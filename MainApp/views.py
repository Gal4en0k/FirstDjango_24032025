from django.shortcuts import render
from django.http import HttpResponse


myfio = "Чухвичёва Г.А."
author = {
    "FirstName": "Иван",
    "SecondName": "Петрович",
    "Family": "Иванов",
    "Phone": "8-923-600-01-02",
    "email": "vasya@mail.ru"
}

def home(request):
    
    text=f""" 
    "<h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>{myfio}</i>" \
    """
    return HttpResponse(text)

def about(request):
    text=f""" 
    Имя: <b>{author["FirstName"]}</b><br>
    Отчество: <b> {author["SecondName"]}</b><br>
    Фамилия: <b>{author["Family"]}</b><br>
    Телефон: {author["Phone"]}<br>
    email:{author["email"]}<br>
    """
    return HttpResponse(text)