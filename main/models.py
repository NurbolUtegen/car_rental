from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    name = models.CharField("Модель", max_length=100)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена в сутки (₽)", max_digits=10, decimal_places=2)
    image = models.ImageField("Фото", upload_to='cars/')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создатель")
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)git add .

    def __str__(self):
        return f"{self.name} — {self.price}₽"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField("Дата начала")
    end_date = models.DateField("Дата окончания")
    created_at = models.DateTimeField("Создано", auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} бронирует {self.car.name}"