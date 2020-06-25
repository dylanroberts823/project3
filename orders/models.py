from django.db import models
from django.conf import settings


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category}"

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.item}, {self.category}"

class Item_Price(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="price")

    SMALL = 'SM'
    LARGE = 'LG'
    SET = 'ST'

    SIZE_CHOICES = [
        (SMALL, 'Small'),
        (LARGE, 'Large'),
        (SET, 'Set'),
    ]
    topping_count = models.IntegerField(default=0,)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, default=SMALL,)
    price = models.FloatField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.item}, {self.size}, {self.topping_count} topppings at {self.price}"

class Category_Topping(models.Model):
    topping = models.CharField(max_length=64)
    category = models.ForeignKey(Category, related_name='toppings', on_delete=models.CASCADE,)
    price = models.FloatField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.topping} topping, {self.category}, {self.price}"

class Item_Topping(models.Model):
    topping = models.CharField(max_length=64)
    item = models.ManyToManyField(Item, related_name = 'toppings')
    price = models.FloatField(max_length=10)

    def __str__(self):
        return f"{self.topping}, {self.item}, {self.price}"

class Ticket(models.Model):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    item_price = models.ForeignKey(Item_Price, on_delete=models.DO_NOTHING, )
    cat_topping = models.ManyToManyField(Category_Topping, blank=True)
    item_topping = models.ManyToManyField(Item_Topping, blank=True)

    def __str__(self):
        return f"{self.item}"

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    date = models.DateField(auto_now=True)
    order = models.ManyToManyField(Ticket)

    CARTED = 'CA'
    PLACED = 'PL'
    PREPARING = 'PR'
    READY = 'RE'
    DELIVERED = 'DE'
    CANCELLED_BY_CUSTOMER = 'CC'
    CANCELLED_BY_RESTAURANT = 'CR'
    STATUS_CHOICES = [
        (CARTED, 'Carted'),
        (PLACED, 'Placed'),
        (PREPARING, 'Preparing'),
        (READY, 'Ready'),
        (DELIVERED, 'Delivered'),
        (CANCELLED_BY_CUSTOMER, 'Cancelled by customer'),
        (CANCELLED_BY_RESTAURANT, 'Cancelled by restaurant'),
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=CARTED,)

    def __str__(self):
        return f"{self.status}: {self.user}'s order on {self.date}"
