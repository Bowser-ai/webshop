from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=300)
    img = models.ImageField(upload_to='shop_pics')
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name;
