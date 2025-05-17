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
            login(request, user)
            return redirect('home')
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
            return redirect('home')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form, 'car': car})

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})


from .forms import CarForm
from django.contrib.auth.decorators import login_required

@login_required
def create_ad(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.created_by = request.user
            car.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'create_ad.html', {'form': form})

from django.shortcuts import render
from .models import Car
from .forms import LocationSearchForm
from math import radians, cos, sin, asin, sqrt

# Функция для расчёта расстояния между двумя точками
def haversine(lon1, lat1, lon2, lat2):
    # переводим координаты в радианы
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # формула гаверсинуса
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6371 * c  # радиус Земли в км
    return km

def search_nearby(request):
    form = LocationSearchForm(request.GET or None)
    results = []

    if form.is_valid():
        user_lat = form.cleaned_data['latitude']
        user_lon = form.cleaned_data['longitude']
        radius = form.cleaned_data['radius']

        all_cars = Car.objects.exclude(latitude__isnull=True, longitude__isnull=True)

        for car in all_cars:
            dist = haversine(user_lon, user_lat, car.longitude, car.latitude)
            if dist <= radius:
                car.distance = round(dist, 2)
                results.append(car)

        results.sort(key=lambda x: x.distance)

    return render(request, 'search_nearby.html', {
        'form': form,
        'results': results,
    })