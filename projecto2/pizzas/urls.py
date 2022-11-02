from xml.etree.ElementInclude import include
from django.urls import path
from pizzas.views import cardapio, inicial, new_pizza, toppings, new_topping
from users.views import my_login_view

urlpatterns = [
    path('', inicial, name='home_page'),
    path('cardapio/', cardapio, name='cardapio'),
    path('toppings/<int:pizza_id>/', toppings, name='toppings' ),
    path('new_pizza/', new_pizza, name='new_pizza'),
    path('new_topping/<int:pizza_id>/', new_topping, name='new_topping'),
    path('login/', my_login_view, name='login'),
    # path('edit_entry/<int:entry_id>/', edit_entry, name='edit_entry'),
]
