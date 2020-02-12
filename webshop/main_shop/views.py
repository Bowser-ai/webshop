from django.shortcuts import render, reverse
from django.contrib.sessions.models import Session
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import CreateView
from .models import Shop, Order as ShopOrder
from users.forms import OrderForm

def shop_home(request):
    return render(request, 'main_shop/main.html')

def shop(request):
    shop_items = Shop.objects.order_by('name')
    context = {'shop_items' : shop_items}

    if 'cart' in request.session:
        total_amount = __getTotalAmountFromCart(request)
        context['total_amount'] = total_amount
    else :
        request.session['cart'] = {}

    return render(request, 'main_shop/shop.html', context)

@login_required
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
    return HttpResponseRedirect(reverse('main_shop:shop'))

def __getTotalAmountFromCart(request):
    cart = request.session['cart']
    return sum([cart[key]['amount'] for key in cart.keys()])

class Order(CreateView):
    template_name = 'users/order.html'
    form_class = OrderForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            for key in request.session['cart'].keys():
                order = ShopOrder.objects.create(
                    user=request.user,
                    shop_item = Shop.objects.get(id=key),
                    amount = request.session['cart'][key]['amount'],
                    street = form.cleaned_data['street'],
                    zip = form.cleaned_data['zip'],
                    country = form.cleaned_data['country'],
                    payment = form.cleaned_data['payment']
                    )
            request.session['cart'] = {}
            return HttpResponseRedirect(reverse('main_shop:shop'))
        else:
            return self.form_invalid(form)
