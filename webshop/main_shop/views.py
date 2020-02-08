from django.shortcuts import render, reverse
from django.contrib.sessions.models import Session
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import CreateView
from .models import Shop, Order;

def shop_home(request):
    return render(request, 'main_shop/main.html')

def shop(request):
    shop_items = Shop.objects.all()
    context = {'shop_items' : shop_items}

    if 'cart' in request.session:
        total_amount = __getTotalAmountFromCart(request)
        context['total_amount'] = total_amount
    else :
        request.session['cart'] = {}

    return render(request, 'main_shop/shop.html', context)

def cart(request):
    products = []
    cart = request.session['cart']

    total_price = 0.0
    for product_id in cart.keys():
        amount = cart[product_id]['amount']
        product_model = Shop.objects.get(id=product_id)
        total_price += amount * product_model.price

        product = {
        'meta' : product_model,
        'amount' : amount
        }
        products.append(product)

    context = {
    'products' : products,
    'total_price' : total_price
    }

    return render(request, 'main_shop/cart.html', context)

def ajaxShop(request):
    shop_item_id = request.POST['product_id']
    shop_item = Shop.objects.get(id=shop_item_id)

    if shop_item_id in request.session['cart']:
        amount = request.session['cart'][shop_item_id]['amount'] + 1
    else :
        amount = 1

    cart = request.session['cart']
    cart[shop_item_id] = {'amount' : amount}
    request.session['cart'] = cart
    total_amount = __getTotalAmountFromCart(request)

    return JsonResponse({'amount' : total_amount})

def cartCancel(request):
    request.session['cart'] = {}
    return HttpResponseRedirect(reverse('shop'))

def __getTotalAmountFromCart(request):
    total_amount = 0

    for key in request.session['cart'].keys():
        total_amount += request.session['cart'][key]['amount']

    return total_amount

class Order(CreateView):
    model = Order
    template_name = 'users/order.html'
    fields = ['street', 'country', 'zip']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shop_items'] = Shop.objects.all()

        return context
