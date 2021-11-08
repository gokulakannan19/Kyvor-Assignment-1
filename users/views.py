from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages


def login_user(request):
    page = "login"

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print("Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print("Username or password is incorrect")

    return render(request, 'users/login-register.html')
