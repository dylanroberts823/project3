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
    small_price = models.FloatField(max_length=10, blank=True, null=True)
    large_price = models.FloatField(max_length=10, blank=True, null=True)
    set_price = models.FloatField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.item}"

class Category_Topping(models.Model):
    topping = models.CharField(max_length=64)
    category = models.ManyToManyField(Category, related_name='toppings')

    def __str__(self):
        return f"{self.topping}"

class Item_Topping(models.Model):
    topping = models.CharField(max_length=64)
    item = models.ManyToManyField(Item, related_name = 'toppings')

    def __str__(self):
        return f"{self.topping}"

class Ticket(models.Model):
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)
    cat_topping = models.ManyToManyField(Category_Topping)
    item_topping = models.ManyToManyField(Item_Topping)

    def __str__(self):
        return f"{self.item}"

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    date = models.DateField(auto_now=True)
    order = models.ManyToManyField(Ticket)

    PLACED = 'PL'
    PREPARING = 'PR'
    READY = 'RE'
    DELIVERED = 'DE'
    CANCELLED_BY_CUSTOMER = 'CC'
    CANCELLED_BY_RESTAURANT = 'CR'
    STATUS_CHOICES = [
        (PLACED, 'Placed'),
        (PREPARING, 'Preparing'),
        (READY, 'Ready'),
        (DELIVERED, 'Delivered'),
        (CANCELLED_BY_CUSTOMER, 'Cancelled by customer'),
        (CANCELLED_BY_RESTAURANT, 'Cancelled by restaurant')
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PLACED,)

    def __str__(self):
        return f"{self.user} ordered {self.order} on {self.date}"
