from django.http import HttpResponse
from django.shortcuts import render

from .models import Categories, Items, Extras

# Create your views here.
def index(request):
    context = {
        "Categories": Categories.objects.all(),
        "Items": Items.objects.all()
    }
    return render(request, "orders/index.html", context)
