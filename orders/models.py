from django.db import models

# Create your models here.
class Categories(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category}"

class Items(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    item = models.CharField(max_length=64)
    small_price = models.FloatField(max_length=10, blank=True, null=True)
    large_price = models.FloatField(max_length=10, blank=True, null=True)
    set_price = models.FloatField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.item}"

class Category_Toppings(models.Model):
    topping = models.CharField(max_length=64)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.topping}"

class Item_Toppings(models.Model):
    topping = models.CharField(max_length=64)
    item = models.ForeignKey(Items, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.topping}"
