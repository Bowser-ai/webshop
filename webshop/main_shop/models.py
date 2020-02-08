from django.db import models
from django.contrib.auth.models import User

class Shop(models.Model):
    name = models.CharField(max_length=300)
    img = models.ImageField(upload_to='shop_pics')
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name;

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    shop_item = models.ForeignKey(Shop, on_delete=models.PROTECT)
    amount = models.IntegerField()

    street = models.CharField(max_length=300)
    zip = models.CharField(max_length=15)
    country = models.CharField(max_length=300)

    class Meta:
        index_together = ['user', 'shop_item']

    def __str__(self):
        return self.user.username + ' ' + self.shop_item.name
