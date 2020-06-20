from django import forms
from django.forms import ModelForm
from .models import Category, Item, Category_Topping, Item_Topping, Order

class ToppingForm(forms.Form):
    def __init__(self, topping_list, *args, **kwargs):
        super(ToppingForm, self).__init__(*args, **kwargs)
        self.fields['topping'] = forms.ChoiceField(choices=topping_list)
