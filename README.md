# FirstDjango_24032025

## Инструкция по развертыванию проекта
1. `python3 -m venv django_venv`

2. `source django_venv/bin/activate`

3. `pip install -r requirements.txt`

4. `python manage.py migrate`

5. `python manage.py runserver`

## Запуск `ipython` в контексте приложения `django`
```
python manage.py shell_plus --ipython 
```
## Выгрузить данные из БД 
#по всем моделям MainApp, только для Item, только для color
```
python manage.py dumpdata MainApp --indent 4 > ./fixtures/items.json
python manage.py dumpdata MainApp.item --indent 4 > ./fixtures/item_only.json
python manage.py dumpdata MainApp.color --indent 4 > ./fixtures/color_only.json
```
## Загрузка данных из БД
```
python manage.py loaddata ./fixtures/items.json
```

## Дополнительно
1. Полезное дополнение для шаблонов `Django`

ext install batisteo.vscode-django

Добавить в `settings.json`

"emmet.includeLanguages": {
    "django-html": "html",
    },
"files.associations": {
    "*.html": "django-html"
    }




