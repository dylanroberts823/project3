from django.urls import path

from . import views

urlpatterns = [
    path("menu/", views.menu, name="menu"),
    path("<int:item_id>", views.select_toppings, name="select_toppings"),
    path("<int:item_id>/select_size", views.select_size, name="select_size"),
    path("<int:item_id>/<int:price_id>/select_toppings", views.select_toppings, name="select_toppings"),
    path("myorders/", views.myorders, name="myorders"),
    path("modify_cart/", views.modify_cart, name="modify_cart"),
]
