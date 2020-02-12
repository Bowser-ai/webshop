from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from main_shop.models import Order, Payment

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class OrderForm(forms.ModelForm):
    payment = forms.ModelChoiceField(queryset=Payment.objects.all())
    class Meta:
        model = Order
        fields = ['street', 'country', 'zip', 'payment']
