from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm

def register(request):

    if request.method != 'POST':
        form = UserRegistrationForm()

    else:
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username = new_user.username,
                    password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('shop_home'));

    return render(request, 'users/register.html', {'form' : form})
