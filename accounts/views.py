from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import views
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import auth
# Create your views here.

def signup(request):
    if request.method == "POST":
        userform = CreateUserForm(request.POST)
        if userform.is_valid():
            userform.save()
            return redirect('home')
    elif request.method == 'GET':
        userform = CreateUserForm()  
    return render(request, 'registration/signup.html', {"userform":userform})