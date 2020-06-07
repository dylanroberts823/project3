from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Category, Item, Category_Topping, Item_Topping, Order

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    context = {
        "user": request.user,
        "Category": Category.objects.all(),
        "Item": Item.objects.all()
    }
    return render(request, "orders/index.html", context)
