from django.contrib import admin

from .models import Categories, Items, Category_Toppings, Item_Toppings

# Register your models here.
admin.site.register(Categories)
admin.site.register(Items)
admin.site.register(Category_Toppings)
admin.site.register(Item_Toppings)
