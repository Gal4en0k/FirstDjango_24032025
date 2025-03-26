from django.db import models

class Color(models.Model):
   name = models.CharField(max_length=32)

   def __repr__(self):
       return f'Color({self.name})'

class Item(models.Model):
    name  = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField() 
    description = models.TextField(max_length=500, default='описание будет добавлено позднее')
    colors = models.ManyToManyField(to=Color)

    def __repr__(self):
        return f'Item({self.name})' 