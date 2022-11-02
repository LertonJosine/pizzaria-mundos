from django.urls import path
from django.contrib.auth.views import LoginView
from .views import my_logout_view, register, my_login_view
from pizzas.views import inicial, cardapio


urlpatterns = [
    path('login/', my_login_view, name='login'),
    path('logout/', my_logout_view, name='logout'),
    path('', inicial, name='home'),
    path('register/', register, name='register'),
    path('cardapio/', cardapio, name='cardapio'),
]
