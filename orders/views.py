from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Category, Item, Category_Topping, Item_Topping, Order

# Create your views here.
def menu(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")
    context = {
        "user": request.user,
        "Category": Category.objects.all(),
        "Item": Item.objects.all()
    }
    return render(request, "orders/menu.html", context)

def myorders(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    context = {
        "user": request.user,
        "Order": Item_Topping.objects.all
    }
    return render(request, "orders/myorders.html", context)

def select_toppings(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    context = {
        "user": request.user,
        "Category": Category.objects.all(),
        "Item": Item.objects.all(),
        "Category_Topping": Category_Topping.objects.all(),
        "Item_Topping": Item_Topping.objects.all(),
        "Order": Item_Topping.objects.all(),
    }
    return render(request, "orders/select_toppings.html", context)
