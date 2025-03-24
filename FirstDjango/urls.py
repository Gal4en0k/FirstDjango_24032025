from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path("product/<int:id>/", views.product)
]
