from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Categories, Items, Category_Toppings, Item_Toppings

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    context = {
        "user": request.user,
        "Categories": Categories.objects.all(),
        "Items": Items.objects.all()
    }
    return render(request, "orders/index.html", context)
