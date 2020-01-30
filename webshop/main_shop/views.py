from django.shortcuts import render


def shop_home(request):
    return render(request, 'main_shop/main.html')
