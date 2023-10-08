from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


# Create your views here.
# acá se crean las vistas
def home(request):
    return render(request, 'home.html')


def singup(request):
    if request.method == 'GET':
        return render(request, 'singup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'singup.html', {
                    'form': UserCreationForm,
                    "error": 'el usuario ya existe broder aaaa'
                })
        return render(request, 'singup.html', {
            'form': UserCreationForm,
            "error": 'password incorrecto po comparini'
        })


def tasks(request):
    return render(request, 'tasks.html')


def singout(request):
    logout(request)
    return redirect('home')


def singin(request):
    if request.method == 'GET':
        return render(request, 'singin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
                    request, username=request.POST['username'],
                     password=request.POST['password'])
        if user is None:
             return render(request, 'singin.html', {
            'form': AuthenticationForm,
            'error': 'Username or password is incorrect'
        })
        else:
             login(request, user)
             return redirect('tasks')    


        
