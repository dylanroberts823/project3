from django.contrib import admin

from .models import Category, Item, Category_Topping, Item_Topping, Order

# Register your models here.
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Category_Topping)
admin.site.register(Item_Topping)
admin.site.register(Order)
