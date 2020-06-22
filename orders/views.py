from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core import serializers

from .models import Category, Item, Category_Topping, Item_Topping, Ticket, Order

# Create your views here.
def menu(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")

    cart = "Empty Cart"
    #If their cart exists, get that information
    if request.session.get('cart', None):
        cart = request.session.get('cart')
        print("Cart exists")
        #Create a list to store the detailed list of items in the ticket
        ticketed_cart = []

        #Loop through the cart to populate the new list
        for ticket in cart:
            cart_item = Ticket.objects.get(id=ticket)
            ticketed_cart.append(cart_item)
        #Make the cart variable equal to ticketed_cart
        cart = ticketed_cart

    context = {
        "user": request.user,
        "Category": Category.objects.all(),
        "Item": Item.objects.all(),
        "Cart": cart,
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

def add_ticket(request, item_id):
    if request.method == 'POST':
        #Create a ticket with the item
        ticket = Ticket.objects.create(item = Item.objects.get(pk=item_id))

        #Add all of the toppings for that item
        for topping in request.POST.getlist('cat_topping'):
            cat_topping = Category_Topping.objects.get(pk=topping)
            ticket.cat_topping.add(cat_topping)
        for topping in request.POST.getlist('item_topping'):
            item_topping = Item_Topping.objects.get(pk=topping)
            ticket.item_topping.add(item_topping)

        #Add the items to the cart
        #If there is no item named cart, create an array with the ticket as the first object in the cart
        if not request.session.get('cart', None):
            request.session["cart"] = [ticket.id]
            print("New cart with: ", request.session.get('cart'))
        #Since there is a cart, add the item to the cart
        else:
            #Get the old cart
            cart = request.session.get("cart")

            #Modify cart to add the new ticket
            cart.append(ticket.id)

            #Replace the old cart object
            request.session["cart"] = cart
            print("Adding to cart, new cart: ", request.session.get("cart"))

        #Go back to the menu
        return HttpResponseRedirect(reverse('menu'))

    #Since it's not a post request, go back to the menu
    else:
        return HttpResponseRedirect(reverse('menu'))
