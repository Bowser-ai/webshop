from django.urls import path
from . import views
from webshop import settings
from django.conf.urls.static import static

urlpatterns = [
        path('', views.shop_home, name='shop_home'),
        path('shop/',views.shop, name='shop')
        ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
