from django.urls import path

from . import views

urlpatterns = [
    path("menu/", views.menu, name="menu"),
    path("<int:item_id>", views.select_toppings, name="select_toppings"),
    path("<int:item_id>/add_to_cart", views.add_to_cart, name="add_to_cart"),
    path("myorders/", views.myorders, name="myorders"),
    path("modify_cart/", views.modify_cart, name="modify_cart"),
]
