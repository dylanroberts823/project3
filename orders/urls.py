from django.urls import path

from . import views

urlpatterns = [
    path("menu/", views.menu, name="menu"),
    path("select_toppings/", views.select_toppings, name="select_toppings"),
    path("myorders/", views.myorders, name="myorders"),
]
