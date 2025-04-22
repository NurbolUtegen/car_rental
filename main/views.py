from django.shortcuts import render, redirect
from .models import Car
from django.contrib.auth import login
from .forms import SignUpForm

def home(request):
    cars = Car.objects.all()
    return render(request, 'home.html', {'cars': cars})


from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # автоматический вход после регистрации
            return redirect('home')  # можно поменять на нужную страницу
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})