from django.shortcuts import render
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

# Create your views here.

def my_login_view(request):
    if request.method == 'GET':
        form = AuthenticationForm()
    else:
        form = AuthenticationForm(data=request.POST)
        user_authenticated = authenticate(username=request.POST['username'], password= request.POST['password'])
        login(request, user_authenticated)
        return HttpResponseRedirect(reverse('home'))

    context = {
        'form':form
    }

    return render(request, 'registration/login.html', context)


def my_logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def register(request):
    if request.method == 'GET':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('home'))
    context = {'form':form}

    return render(request, 'register.html', context)
