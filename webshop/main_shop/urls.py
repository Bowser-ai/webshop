from django.urls import path
from . import views
from webshop import settings
from django.conf.urls.static import static

urlpatterns = [
        path('', views.shop_home, name='shop_home'),
        path('shop/',views.shop, name='shop'),
        path('shop/ajax/', views.ajaxShop, name='ajax_shop'),
        path('shop/cart', views.cart, name='cart'),
        path('shop/cart-cancel', views.cartCancel, name='cart_cancel'),
        path('shop/order', views.Order.as_view(), name='order')
        ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
