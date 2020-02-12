from django.test import TestCase
from .models import Order, Shop
from django.urls import reverse

def setup():
    shop_item_1 = Shop.objects.create(name='sword',
        img='/home/jessica/src/python/webshop/webshop/media/shop_pics/article_2.jpg',
        description='nice sword',
        price=114.99,
        stock=5)
    shop_item_2 = Shop.objects.create(name='football',
        img='/home/jessica/src/python/webshop/webshop/media/shop_pics/article_1.jpg',
        description='nice football',
        price=4.99,
        stock=3)

class ShopHomeTests(TestCase):
    def testPageFound(self):
        response = self.client.get(reverse('main_shop:shop_home'))
        self.assertEqual(response.status_code, 200)

class ShopTests(TestCase):
    def testShopItems(self):
        setup();
        response = self.client.get(reverse('main_shop:shop'))
        self.assertQuerysetEqual(response.context['shop_items'],
        ['<Shop: football>', '<Shop: sword>'])
