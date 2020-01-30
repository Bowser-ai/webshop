from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserRegistrationForm

def register(request):

    if request.method != 'POST':
        form = UserRegistrationForm()

    else:
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main_shop/shop_home'));

    return render(request, 'users/register.html', {'form' : form})
