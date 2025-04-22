from django.shortcuts import render, redirect
from .models import Car, Booking
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


from .forms import BookingForm
from django.contrib.auth.decorators import login_required

@login_required
def book_car(request, car_id):
    car = Car.objects.get(id=car_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.car = car
            booking.user = request.user
            booking.save()
            return redirect('home')  # или на страницу с подтверждением
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form, 'car': car})