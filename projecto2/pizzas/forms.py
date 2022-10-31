from dataclasses import field
from django.forms import ModelForm
from pizzas.models import Pizza, Topping

class PizzaForm(ModelForm):
    class Meta:
        model = Pizza
        fields = ['name']
        labels = {'name': ''}


class ToppingForm(ModelForm):
    class Meta:
        model = Topping
        fields = ['igredients']
        labels = {'igredients': ''}