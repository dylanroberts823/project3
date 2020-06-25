from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core import serializers

from .models import Category, Item, Category_Topping, Item_Topping, Item_Price, Ticket, Order

# Create your views here.
def menu(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")

    #Check if the cart exists from a previous session
    if(Order.objects.filter(user = request.user, status="CA").count() == 0):
        cart = Order.objects.create(user = request.user)
    #Since the cart does not exist, create one
    else:
         cart = Order.objects.get(user = request.user, status="CA")

    #Loop through the cart to populate the cart display
    cart_display = []
    total = 0
    for ticket in cart.order.all():
        #Add the ticket to the display
        cart_display.append(ticket)

        #Add the price for each item
        total += ticket.item_price.price
        for topping in ticket.cat_topping.all():
            total += topping.price
        for topping in ticket.item_topping.all():
            total += topping.price

    cart = cart_display

    context = {
        "user": request.user,
        "Category": Category.objects.all(),
        "Item": Item.objects.all(),
        "Cart": cart,
        "Total": total,
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

def select_size(request, item_id):
    if request.method == 'POST':
        print("Got to post")
        price_id = request.POST.get("size")

        #Go to select toppings
        return redirect('select_toppings', item_id = item_id, price_id = price_id)

    #Since it's not a post request, open select size
    else:
        item = Item.objects.get(pk = item_id)
        context = {
            "Item": item,
            "Sizes": item.price.all(),
            "item_id": item_id
        }
        return render(request, "orders/select_size.html", context)

def select_toppings(request, item_id, price_id):
    if request.method == 'POST':

        #Add all of the toppings for that item
        cat_topping_array = request.POST.getlist('cat_topping')
        item_topping_array = request.POST.getlist('item_topping')

        return add_to_cart(request, item_id, price_id, cat_topping_array, item_topping_array)


    #Since it's not a post request, go back to the menu
    else:
        if not request.user.is_authenticated:
            return render(request, "users/login.html", {"message": None})
        #If method is post, add the item to the cart
        #If method is get, display the page
        #First, check that object exists
        try:
            item = Item.objects.get(pk=item_id)
        except Item.DoesNotExist:
            raise Http404("Item Does Not Exist")
            #Check that the price exists
        try:
            item_price = Item_Price.objects.get(pk=price_id)
        except Item_Price.DoesNotExist:
            raise Http404("Item Does Not Exist")

        if item_price.topping_count == 0:
            return add_to_cart(request, item_id, price_id, [], [])
        context = {
            "item": item,
            "item_toppings": item.toppings.all(),
            "cat_toppings": item.category.toppings.all(),
            "item_price": item_price,
        }
        return render(request, "orders/select_toppings.html", context)

def add_to_cart(request, item_id, price_id, cat_topping, item_topping):
    #Create a ticket for that item
    ticket = Ticket.objects.create(item = Item.objects.get(pk=item_id), item_price = Item_Price.objects.get(pk = price_id))
    for topping in cat_topping:
        ticket.cat_topping.add(topping)
    for topping in item_topping:
        ticket.item_topping.add(topping)

    #Add the item to the order
    cart = Order.objects.get(user = request.user, status="CA")
    cart.order.add(ticket)

    #Go back to the menu
    return HttpResponseRedirect(reverse('menu'))

def remove_from_cart(request, ticket_id):
    ticket = Ticket.objects.get(pk = ticket_id)
    cart = Order.objects.get(user = request.user, status="CA")
    cart.order.remove(ticket)
    return HttpResponseRedirect(reverse('menu'))

def checkout(request):
    cart = Order.objects.get(user = request.user, status="CA")
    cart.status="PL"
    cart.save()
    return HttpResponseRedirect(reverse('menu'))

def confirmation(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")

    cart = Order.objects.get(user = request.user, status="CA")
    #Loop through the cart to populate the cart display
    cart_display = []
    total = 0
    for ticket in cart.order.all():
        #Add the ticket to the display
        cart_display.append(ticket)

        #Add the price for each item
        total += ticket.item_price.price

    cart = cart_display
    context = {
        "user": request.user,
        "Category": Category.objects.all(),
        "Item": Item.objects.all(),
        "Cart": cart,
        "Total": total,
    }
    return render(request, "orders/confirmation.html", context)
