from django.shortcuts import render
from django.contrib.sessions.models import Session
from .models import Shop;

def shop_home(request):
    return render(request, 'main_shop/main.html')

def shop(request):
    shop_items = Shop.objects.all()
    context = {'shop_items' : shop_items}
    if 'cart' in request.session:
        stored_shop_items = request.session['cart']
        context['stored_shop_items'] = stored_shop_items
    return render(request, 'main_shop/shop.html', context)
