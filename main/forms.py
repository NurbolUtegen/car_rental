from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_date', 'end_date']


from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'description', 'price', 'image','latitude', 'longitude']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }