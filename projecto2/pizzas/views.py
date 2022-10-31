from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Pizza
from pizzas.forms import PizzaForm, ToppingForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def inicial(request):
    return render(request, 'index.html')


@login_required
def cardapio(request):
    pizzas = Pizza.objects.all()
    context = {'pizzas':pizzas}
    return render(request, 'cardapio.html', context)

@login_required
def toppings(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {
        'pizza': pizza,
        'toppings': toppings
    }
    return render(request, 'toppings.html', context)

@login_required
def new_pizza(request):
    if request.method == 'GET':
        form = PizzaForm()
    
    elif request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cardapio'))
    context = {
        'form': form
    }

    return render(request, 'new_pizza.html', context)

@login_required
def new_topping(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method == 'GET':
        form = ToppingForm()
    elif request.method == 'POST':
        form = ToppingForm(request.POST)
        new_topping = form.save(commit=False)
        new_topping.pizza = pizza
        new_topping.save()
        return HttpResponseRedirect(reverse('toppings', args=[pizza_id]))
    context ={
        'pizza': pizza,
        'form':  form
    }
    return render(request, 'new_topping.html', context)

# @login_required
# def edit_entry(request, entry_id):
#     entry = Entry.objects.get(id=entry_id)
    
