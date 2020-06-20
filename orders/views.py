from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core import serializers

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

def select_toppings(request, item_id):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    #If method is post, add the item to the cart
    #If method is get, display the page
    #First, check that object exists
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        raise Http404("Item Does Not Exist")
    context = {
        "item": item,
        "item_toppings": item.toppings.all(),
        "cat_toppings": item.category.toppings.all()
    }
    return render(request, "orders/select_toppings.html", context)


def modify_cart(request):
    context = {
        "item": request.POST.get('quantity-data-item'),
        "quantity": request.POST.get('quantity')
    }
    return render(request, "orders/test.html", context)

def add_to_cart(request, item_id)
    user =
