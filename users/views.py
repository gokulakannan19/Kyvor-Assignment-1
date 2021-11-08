from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# from django.contrib import messages
from .forms import CustomUserCreationForm


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


@login_required(login_url='login-user')
def logout_user(request):
    logout(request)
    print("user was successfully logged out")
    # messages.error(request, "User was successfully logged out")
    return redirect('login-user')


def register_user(request):
    page = "register"

    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            # messages.success(request, "User was created successfully")
            print("User was created successfully")

            login(request, user)
            return redirect('home')

        else:
            # messages.error(request, "An error occured in registration")
            print("An error occured")
    context = {
        'page': page,
        'form': form,
    }
    return render(request, 'users/login-register.html', context)
