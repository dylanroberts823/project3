from django.db import models

# Create your models here.
class Categories(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category}"

class Extras(models.Model):
    extra = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.extra}"

class Items(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    item = models.CharField(max_length=64)
    small_price = models.FloatField(max_length=10, blank=True)
    large_price = models.FloatField(max_length=10, blank=True)
    set_price = models.FloatField(max_length=10, blank=True)
    extras = models.ManyToManyField(Extras)

    def __str__(self):
        return f"{self.item}"
