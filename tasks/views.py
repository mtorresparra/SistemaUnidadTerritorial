from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
#acá se crean las vistas
def home(request):
    return render(request, 'home.html')

def singup(request):
    return render(request, 'singup.html')